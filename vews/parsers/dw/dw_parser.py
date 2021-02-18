import requests
import re
from bs4 import BeautifulSoup

from vews.parsers.write_news import write_news
from app import client


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find("div", id="bodyMover").find(class_="teaserContentWrap").find("a").get("href")
    return data


def get_text(html):
    soup = BeautifulSoup(html, "lxml")
    article = soup.find(id="bodyContent")
    title = article.find("h1").text
    intro = article.find("p", class_="intro").text
    img = article.find("img").get("src")
    demo_body = article.find("div", class_="group")
    txt = re.compile(r'\w+=\s*')
    body = txt.sub("", demo_body.text)

    return {"title": title, "intro": intro, "img": img, "body": body}



def dw(url):
    html = get_html(url)
    data = get_data(html)
    html_content = get_html(url + data)
    text = get_text(html_content)

    write_news("dw", text, url)
