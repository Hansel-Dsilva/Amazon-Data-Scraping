# base_url = 'https://www.amazon.in/s?k=men+tshirts&page=2&qid=1568399887&ref=sr_pg_' + str(page)
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


def scrape():
    productData = pd.DataFrame(columns=['Product_name', 'Price', 'Date', 'Time'])
    for page in range(1,4):
        list_of_rows = []
        base_url = 'https://www.amazon.in/s?k=tommy+hilfiger+t+shirt+for+men&page=' + str(page)
        # print(base_url)

        # Request URL and Beautiful Parser
        r = requests.get(base_url, headers={"User-Agent":"Defined"})
        soup = BeautifulSoup(r.text, "html.parser")

        #all_product = soup.find_all(lambda tag: tag.name == 'span')
        class_ = ["a-size-base-plus a-color-base a-text-normal", "a-price-whole"]
        all_product = soup.find_all('span', class_)
        print(len(all_product))

        attr = 'Product_name'
        row = {}
        for item in all_product:
            #row = [{'Product_name' : np.nan, 'Price' : np.nan, 'Date' : np.nan, 'Time' : np.nan}]
            if attr == 'Product_name':
                attr = 'Price'
                row.update({'Product_name' : str(item.string)})
            elif attr == 'Price':
                attr = 'Product_name'
                row.update({'Price' : str(item.string)})
                list_of_rows.append(row)
                row = {}
        productData.append(list_of_rows)
    return productData


if __name__ == "__main__":
    print(scrape())
