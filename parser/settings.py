import fake_useragent


user = fake_useragent.UserAgent().random

header = {"user-agent": user}

#root_link = "https://economapteka.ru/catalog/prochie-lechebno-profilakticheskie-sredstva/dlya-nervnoy-sistemy/sedativnye-serdtse/"
root_link = "https://economapteka.ru/catalog/krasota-i-zdorove/vitaminki/"