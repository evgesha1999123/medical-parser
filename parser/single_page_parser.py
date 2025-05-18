#parses links for each item on page
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from parser.settings import user, header, root_link


def paginator(link:str):
    try:
        response = requests.get(link, headers=header, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'lxml')

        last_page_from_tag = soup.find_all("a", class_="pagination__item")[-1]
        last_page_index = int(last_page_from_tag.get("data-page"))

        paginated_links = []
        for i in range(1, last_page_index + 1):
            paginated_links.append(link + f"?PAGE={i}")
        return paginated_links


    except requests.RequestException as e:
        print(f"Error on {link}: <{e}>")

def parse_links(link) -> list[str]:
    responce = requests.get(link, headers=header).text
    soup = BeautifulSoup(responce, "lxml")

    raw_html_data = soup.find_all("a", class_="c-product__name")
    #join all href links for each link in all <a tags
    links = [urljoin(root_link, link["href"]) for link in raw_html_data] 
    return links

if __name__ == "__main__":
    print(paginator("https://economapteka.ru/catalog/krasota-i-zdorove/vitaminki/"))