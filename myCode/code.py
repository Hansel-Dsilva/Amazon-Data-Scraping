# base_url = 'https://www.amazon.in/s?k=men+tshirts&page=2&qid=1568399887&ref=sr_pg_' + str(page)

import pandas as pd

def scrape():
    from bs4 import BeautifulSoup
    import requests
    from datetime import datetime
    from pathlib import Path

    productData = pd.DataFrame(columns=['Product_name', 'Price', 'Date', 'Time'])
    for page in [1,2,3]:
        list_of_rows = []
        base_url = 'https://www.amazon.in/s?k=tommy+hilfiger+t+shirt+for+men&page=' + str(page)
        # print(base_url)

        # Request URL and Beautiful Parser
        r = requests.get(base_url, headers={"User-Agent":"Defined"})
        soup = BeautifulSoup(r.text, "html.parser")

        #all_product = soup.find_all(lambda tag: tag.name == 'span')
        class_ = ["a-size-base-plus a-color-base a-text-normal", "a-price-whole"]
        all_product = soup.find_all('span', class_)
        print('Products on page ' + str(page) + ' : ' + str(len(all_product)))

        row = {}
        for item in all_product:
            if item.attrs['class'] == ['a-size-base-plus', 'a-color-base', 'a-text-normal']:
                row.update({'Product_name' : str(item.string)})
            elif item.attrs['class'] == ['a-price-whole']:
                row.update({'Price' : str(item.string)})
                row.update({'Date': str(datetime.today().strftime('%Y-%m-%d'))})
                row.update({'Time': "{0:%H:%M:%S}".format(datetime.now())})
                list_of_rows.append(row)
                row = {}
        productData = productData.append(list_of_rows)

    filename = Path(r"C:\Users\HanselAIO\PycharmProjects\dataScraping\myData") / ("{0:%Y-%m-%d_%H:%M:%S}".format(datetime.now()) + '.csv')
    #productData.to_csv(r'C:\Users\HanselAIO\PycharmProjects\dataScraping\myCode\data\file2.csv', mode="w+")
    #csv_file = open("data"+"\{0:%Y-%m-%d_%H:%M:%S}".format(datetime.now())+".csv", mode="w+")

    base_path = Path(__file__).parent
    csv_name = "file" + "{0:%Y-%m-%d_%H-%M-%S}".format(datetime.now()) + ".csv"
    file_path = (base_path / ("../myData/" + csv_name)).resolve()
    productData.to_csv(file_path, mode="w+")
    return productData


if __name__ == "__main__":
    print(scrape())
