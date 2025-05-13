import requests
from bs4 import BeautifulSoup
import datetime
import time
import pandas as pd

from parser.settings import user, header


def get_current_date() -> str:
    return datetime.date.today().isoformat()

def get_current_time() -> str:
    cur_time_unformatted = time.time()
    local_time = time.localtime(cur_time_unformatted)
    formatted_cur_time = time.strftime("%H:%M:%S", local_time)
    return formatted_cur_time

def get_page_data(current_time:str, current_date:str, link:str) -> dict[str, str]:
    #link = "https://economapteka.ru/catalog/product/korvalol-fitokomfort-tab-20/?listName=%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B%20%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0"
    responce = requests.get(link, headers=header).text
    soup = BeautifulSoup(responce, "lxml")

    res_pharmacy_name = soup.find("span", class_="copy").text

    block_medicine_category = soup.find("ul", class_="list list--bar breadcrumbs breadcrumbs--top")
    res_medicine_category = block_medicine_category.find_all("span", itemprop="name")[4].text

    block_medicine_name = soup.find("div", class_="article__header --without-margin-top")
    res_medicine_name = block_medicine_name.find("h1", class_="c-product-card__title").text

    block_dosage = soup.find("div", class_="text-list")
    res_dosage = block_dosage.find_all("div", class_="text-list__item")[12].text

    res_price = soup.find("div", class_="c-product-card__price").text

    block_manufacturer = soup.find("div", class_="c-product-card__about")
    res_manufacturer = block_manufacturer.find("div", class_="c-product-card__about-item").text

    return {
        "link": link,
        "date": current_date,
        "time": current_time,
        "pharmacy": res_pharmacy_name,
        "category": res_medicine_category,
        "medicament": res_medicine_name,
        "dosage": res_dosage,
        "price": res_price,
        "manufacturer": res_manufacturer
    }

if __name__ == "__main__":
    pd.DataFrame(data=[get_page_data(get_current_time(), get_current_date())], index=None).to_excel("result.xlsx", index=None)