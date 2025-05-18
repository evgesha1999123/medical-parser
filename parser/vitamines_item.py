import requests
from bs4 import BeautifulSoup
import pandas as pd
from numpy.ma.extras import median

from parser.sedatives_for_heart_item import get_page_data
from parser.settings import user, header
from parser.utils.timestamp import get_current_time, get_current_date
import re

def get_vitamine_item_data(link, current_date, current_time):
    form = ""
    dosage = ""
    num = ""

    responce = requests.get(link, headers=header).text
    soup = BeautifulSoup(responce, "lxml")

    raw_pharmacy_name = soup.find("span", class_="copy").text
    pharmacy_name = raw_pharmacy_name = re.findall(r'«(.*?)»', raw_pharmacy_name)[0]

    res_medicine_name = soup.find("h1", class_="c-product-card__title").text

    _medicament = soup.find("h1", class_="c-product-card__title").text.strip().split(" ")

    counter = 0
    sep_index_for_name = len(_medicament)
    for word in _medicament:
        if word in {"капс", "таб", "фл"}:
            form = word
            sep_index_for_name = counter
        if word[0].isnumeric():
            dosage = word
        if word[0].startswith("№"):
            num = word
        counter += 1

    medicament = " ".join(_medicament[:sep_index_for_name])

    block_medicine_category = soup.find("ul", class_="list list--bar breadcrumbs breadcrumbs--top")
    category = block_medicine_category.find_all("span", itemprop="name")[4].text

    price = soup.find("div", class_="c-product-card__price").text.strip().replace("Р","")

    manufacturer = soup.find("div", class_="c-product-card__about-item").text.split(": ")[-1]

    print(medicament)


    return {
        "link": link,
        "date": current_date,
        "time": current_time,
        "pharmacy": pharmacy_name,
        "category": category,
        "medicament": medicament,
        "form": form,
        "dosage": dosage,
        "num": num,
        "price": price,
        "manufacturer": manufacturer
    }



if __name__ == '__main__':
    get_vitamine_item_data("https://economapteka.ru/catalog/product/doppelgerts-vip-l-arginin-kaps-900mg-120-2/", get_current_date(), get_current_time())