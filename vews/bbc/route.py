from  flask import Blueprint, render_template

from config import URL_BBC as url
from .task import main

bbc = Blueprint("bbc", __name__)

@bbc.route("/", methods=["GET"])
def news_page():
    article = main(url)
    return render_template("bbc/news_page.html", article=article)