import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soap = BeautifulSoup(html, "lxml")
    data = soap.find("section", id="main").find("a")
    return data


def get_link(url, data):
    link = url + data.get("href")
    return link


def get_img(html):
    soup = BeautifulSoup(html, "lxml")
    article = soup.find("section", id="main")
    demo_body = article.find("div", class_="body js-mediator-article")
    img = demo_body.find("img").get("src")
    return img


def get_title(data):
    title = data.find("h3").text
    return title


def n_pluse_one(url):
    html = get_html(url)
    data = get_data(html)
    title = get_title(data)
    link = get_link(url, data)
    html = get_html(link)
    img = get_img(html)
    previe = {"name": "n+1", "img": img, "title": title, "link": url, "full_news": "n_plus.news_page"}

    return previe

