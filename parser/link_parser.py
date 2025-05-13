import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

from parser.settings import user, header


root_link = "https://economapteka.ru/catalog/prochie-lechebno-profilakticheskie-sredstva/dlya-nervnoy-sistemy/sedativnye-serdtse/"

def parse_links() -> list[str]:
    responce = requests.get(root_link, headers=header).text
    soup = BeautifulSoup(responce, "lxml")

    raw_html_data = soup.find_all("a", class_="c-product__name")
    #join all href links for each link in all <a tags
    links = [urljoin(root_link, link["href"]) for link in raw_html_data] 
    return links

if __name__ == "__main__":
    print(parse_links())