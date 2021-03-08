import requests
from bs4 import BeautifulSoup

from views.parsers.write_news import write_news


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find("section", class_="module module--promo").find("a", class_="block-link__overlay-link").get("href")
    return data


def get_body(list):
    string = ""
    for line in list:
        string += line.text.strip()
    return string


def get_text(html):
    soup = BeautifulSoup(html, "lxml")
    article = soup.find("article", class_="ssrcss-5h7eao-ArticleWrapper e1nh2i2l0")
    title = article.find("h1", id="main-heading").text
    demo_body = article.find_all("p")
    img = article.find("img").get("src")
    body = get_body(demo_body)
    return {"title": title, "img": img, "body": body}


def bbc(url):
    html = get_html(url)
    data = get_data(html)
    html = get_html(url + data)
    text = get_text(html)

    write_news("bbc", text, url)
