from flask import Blueprint, render_template

from ..models import News

general = Blueprint("general", __name__)

@general.route("/", methods=["GET"])
def general_page():
    content = News.query.all()
    return render_template("general/general.html", content=content)

