from click import echo
from flask import Blueprint, render_template

from app.services.service import fetch_data

main = Blueprint("main", __name__)


@main.route("/")
def index():
    news = fetch_data(1) or {}
    return render_template("index.html", **news)