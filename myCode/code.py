# base_url = 'https://www.amazon.in/s?k=men+tshirts&page=2&qid=1568399887&ref=sr_pg_' + str(page)
from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape():
    productData = pd.DataFrame()
    for page in range(1,4):

        base_url = 'https://www.amazon.in/s?k=men+tshirts&page=2&qid=1568399887&ref=sr_pg_' + str(page)
        # print(base_url)

        # Request URL and Beautiful Parser
        r = requests.get(base_url, headers={"User-Agent":"Defined"})
        soup = BeautifulSoup(r.text, "html.parser")

        #all_product = soup.find_all(lambda tag: tag.name == 'span')
        class_ = ["a-size-base-plus a-color-base a-text-normal", "a-price-whole", "a-size-base-plus a-color-base"]
        all_product = soup.find_all('span', class_)
        #print(len(all_product))

        counter = 1
        for item in all_product:
            d = {}

        d['Brand'] = item.string


        l.append(d)
    return l


if __name__ == "__main__":
    print(scrape())
