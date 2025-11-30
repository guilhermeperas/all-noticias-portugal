from click import echo
from flask import Blueprint, render_template, request

from app.services.service import fetch_data

main = Blueprint("main", __name__)

@main.route("/")
def index():
    fetch_data()
    return render_template("index.html")
