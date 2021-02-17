from flask import Blueprint, render_template

from config import URL_PLUS_ONE as url
from .task import main

n_plus = Blueprint("n_plus", __name__)


@n_plus.route("/n+1", methods=["GET"])
def news_page():
    article = main(url)
    return render_template("nplusone/news_page.html", article=article)
