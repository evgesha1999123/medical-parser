import fake_useragent


user = fake_useragent.UserAgent().random
header = {"user-agent": user}
main_link = "https://economapteka.ru/catalog/krasota-i-zdorove/vitaminki/"
links = []