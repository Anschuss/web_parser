from flask import Blueprint, render_template

from config import URL_SPIEGEL as url
from .task import main

spiegel = Blueprint("spiegel", __name__)


@spiegel.route("/", methods=["GET"])
def news_page():
    article = main(url)
    return render_template("spiegel/news_page.html", article=article)