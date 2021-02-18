import requests
import re
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find("main", id="Inhalt").find("a").get("href")
    return data


def normaliaze_body(demo_body):
    txt = re.compile(r'(<[^>]*>)')
    text = txt.sub("", str(demo_body))
    for i in ["[", "]"]:
        body = text.replace(i, "")
    return body


def normalize_title(string):
    res = string.split("Plus")
    del res[0]
    txt = re.compile(r'\w+=\s*[^\n]')
    title = txt.sub("", res[0])
    return title


def get_text(html):
    soup = BeautifulSoup(html, "lxml")
    article = soup.find("main", id="Inhalt")
    demo_title = article.find("article", class_="bg-white shadow").find("span", class_="font-brandUI font-extrabold lg:text-7xl md:text-5xl sm:text-4xl leading-tight").text
    title = normalize_title(demo_title)
    intro = article.find("div", class_="RichText RichText--sans leading-loose lg:text-xl md:text-xl sm:text-l lg:mb-32 md:mb-32 sm:mb-24").text
    img = article.find("div", class_="relative").find("img").get("src")
    demo_body = article.find("div", class_="clearfix lg:pt-32 md:pt-32 sm:pt-24 md:pb-48 lg:pb-48 sm:pb-32").find_all(
        "p")
    body = normaliaze_body(demo_body)
    return {"title": title, "intro": intro, "img": img, "body": body}


def main(url):
    html = get_html(url)
    data = get_data(html)
    html_article = get_html(data)
    text = get_text(html_article)

    text["link"] = data

    return text
