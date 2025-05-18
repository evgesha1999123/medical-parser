import pandas as pd

from parser.settings import root_link
from parser.utils.timestamp import get_current_time, get_current_date

from parser.single_page_parser import parse_links, paginator
#from parser.sedatives_for_heart_item import get_page_data
from parser.vitamines_item import get_vitamine_item_data


if __name__ == "__main__":
    current_time = ""
    current_date = ""

    paginated_links = paginator(root_link)
    payload = []
    counter = 0
    for page in paginated_links:
        links_to_items = parse_links(page)
        for link in links_to_items:
            try:
                current_time = get_current_time()
                current_date = get_current_date()

                payload.append(get_vitamine_item_data(link, current_date, current_time))
                counter += 1
                print(f"{counter}. Successful: {link} [{current_time}]")
            except Exception as error:
                print(f"<{error}> on {link}, skipping [{current_time}]")
                continue
    pd.DataFrame(payload).to_excel("tab_new.xlsx", index=False)