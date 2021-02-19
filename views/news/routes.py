from flask import Blueprint, render_template
from ..models import News

news = Blueprint("news", __name__)


@news.route("/<string:name>")
def news_page(name):
    news = News.query.filter(News.name == name).first()
    return render_template("news/news_page.html", news=news)
