import pathlib
from flask import Blueprint, render_template
import pandas as pd


home_page_blueprint = Blueprint("home_page", __name__)

file_path = pathlib.Path("data/endpoints.csv")
df = pd.read_csv(filepath_or_buffer=file_path, delimiter=",")


@home_page_blueprint.route("/")
def home_page():
    return render_template(template_name_or_list="home_page.html",
                           data=df.to_html(index=False))
