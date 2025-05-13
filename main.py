import requests
from bs4 import BeautifulSoup
import datetime
import time
import pandas as pd

from parser.settings import user, header
from parser.link_parser import parse_links
from parser.single_page_parser import (
    get_current_date, 
    get_current_time,
    get_page_data,
)


if __name__ == "__main__":
    links = parse_links()
    payload = []
    for link in links:
        try:
            # print(link)
            # print(get_page_data(get_current_time(), get_current_date(), link))
            payload.append(get_page_data(get_current_time(), get_current_date(), link))
        except:
            continue
    pd.DataFrame(payload).to_excel("tab.xlsx", index=None)