from flask import Blueprint, render_template
from .run_pars import get_all

from app import client

general = Blueprint("general", __name__)


@general.route("/", methods=["GET", "POST"])
def general_page():
    content = get_all.delay()
    return render_template("general/general.html", content=content)
