import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find("section", class_="module module--promo")
    return data


def get_content(url, data):
    title = data.find("a").text
    link = url + data.find("a").get("href")
    img = data.find("img").get("src")
    return {"title": title, "img": img, "ulr": link, "full_news": "bbc.news_page"}


def bbc(url):
    html = get_html(url)
    data = get_data(html)
    content = get_content(url, data)
    content["name"] = "bbc"
    return content


