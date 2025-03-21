import requests
from bs4 import BeautifulSoup

#Строго главную страницу (index) файл
URL = "https://rezka.ag/"

#HEADERS - это внутренние данные сайта указываем для того что мы не являемся роботом
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
}

#1 создание запроса
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

#2 Получение данных через html (Консоль разработчика)
def get_data(html):
    bs = BeautifulSoup(html, features="html.parser")
    items = bs.find_all("div", class_="b-content__inline_item")
    rezka_list = []
    for item in items:
        title = item.find("div", class_='b-content__inline_item-link').get_text(strip=True)
        image = URL + item.find("div", class_="b-content__inline_item-cover").find("img").get("src")
        rezka_list.append({
            "title": title,
            "image": image,

        })
    return rezka_list

#3 Функционал парсинга и объединение 2х функций в 1
def parsing_rezka():
    response = get_html(URL)
    if response.status_code == 200:
        rezka_list2 = []
        for page in range(1,2):
            response = get_html("https://rezka.ag/films/", params={'page': page})
            rezka_list2.extend(get_data(response.text))
        return  rezka_list2
    else:
        raise Exception("error in parsing")

#print(parsing_rezka())
