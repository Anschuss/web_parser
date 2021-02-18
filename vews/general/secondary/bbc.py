import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find("section", class_="module module--promo")
    return data


def get_content(data):
    title = data.find("a").text
    img = data.find("img").get("src")
    return {"title": title, "img": img}


def bbc(url):
    html = get_html(url)
    data = get_data(html)
    content = get_content(data)
    content["name"] = "bbc"
    content["full_news"] = "bbc.news_page"
    return content


