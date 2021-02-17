from flask import Blueprint, render_template


from .task import main

n_plus = Blueprint("n_plus", __name__)


@n_plus.route("/n+1", methods=["GET"])
def news_page(url):
    article = main(url)
    return render_template("nplusone/news_page.html", article=article)
