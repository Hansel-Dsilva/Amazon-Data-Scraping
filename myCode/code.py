# base_url = 'https://www.amazon.in/s?k=men+tshirts&page=2&qid=1568399887&ref=sr_pg_' + str(page)
from bs4 import BeautifulSoup
import requests


def scrape():
    l = []
    for page in range(3):
        page = page + 1
        base_url = 'https://www.amazon.in/s?k=men+tshirts&page=2&qid=1568399887&ref=sr_pg_' + str(page)
        # print(base_url)

        # Request URL and Beautiful Parser
        r = requests.get(base_url, headers={"User-Agent":"Defined"})
        soup = BeautifulSoup(r.text, "html.parser")

        all_product = soup.find_all(lambda tag: tag.name == 'div')

        all_product = soup.find_all(lambda tag: tag.name == 'span' and tag.get('class') == ['a-price-whole'])
        print(len(all_product))

        for item in all_product:
            d = {}

            # image
            product_image = item.find("img", {"class":"product-media__img"})
            # image = image.text.replace('\n', "").strip()
            product_image = product_image['src']
            d['product_image'] = product_image

            # name & link
            product_name = item.find("a", {"class":"product__name"})
            product_link = 'https://www.bukalapak.com' + str(product_name.get('href'))
            product_name = product_name.text.replace('\n', "").strip()
            d['product_link'] = product_link
            d['product_name'] = product_name

            # price
            product_price = item.find("span", {"class":"amount"})
            product_price = product_price.text.replace('\n', "").strip()
            d['product_price'] = 'Rp' + product_price

            # review
            product_review = item.find("a", {"class":"review__aggregate"})
            try:
                product_review = product_review.text
                d['product_review'] = int(product_review)
            except:
                d['product_review'] = 0

            # link
            # product_link = item.find("a", {"class":"product-media__link"}, href=True)
            # product_link = 'https://www.bukalapak.com' + str(product_link.get('href'))
            # d['product_link'] = product_link

            l.append(d)

    return l


if __name__ == "__main__":
    print(scrape())
