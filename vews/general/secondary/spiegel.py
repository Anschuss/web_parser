import requests
import re
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find("main", id="Inhalt").find("article", class_="rounded-b overflow-hidden")
    return data


def normalize_title(string):
    res = string.split("Plus")
    del res[0]
    txt = re.compile(r'\w+=\s*[^\n]')
    title = txt.sub("", res[0])
    return title


def get_content(data):
    img = data.find("img").get("src")
    demo_title = data.find("header").find("span", class_="block font-brandUI font-extrabold lg:text-5xl md:text-5xl sm:text-3xl leading-tight mb-12").text
    title = normalize_title(demo_title)
    return {"title": title, "img": img}


def spiegel(url):
    html = get_html(url)
    data = get_data(html)
    preview = get_content(data)
    preview["name"] = "spiegel"
    preview["full_news"] = "spiegel.news_page"

    return preview
