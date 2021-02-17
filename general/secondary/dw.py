import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    data = soup.find("div", id="bodyContent").find("div", class_="col4a")
    return data


def get_content(data):
    title = data.find("h2").text
    img = data.find("img").get("src")
    return {"title": title, "img": img}


def dw(url):
    html = get_html(url)
    data = get_data(html)
    content = get_content(data)
    content["name"] = "dw"
    content["full_news"] = "dw.news_page"
    return content


