from flask import Blueprint, render_template

from config import URL_DW as url
from .task import dw

dw_page = Blueprint("dw", __name__)


@dw_page.route("/", methods=["GET"])
def news_page():
    article = dw(url)
    return render_template("dw/news_page.html", article=article)
