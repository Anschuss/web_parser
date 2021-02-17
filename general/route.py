from flask import Blueprint, render_template
from .run_pars import get_all

general = Blueprint("general", __name__)


@general.route("/", methods=["GET", "POST"])
def general_page():
    content = get_all()
    return render_template("general/general.html", content=content)
