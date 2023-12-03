from flask import Blueprint, render_template

home_page_blueprint = Blueprint("home_page", __name__)


@home_page_blueprint.route("/")
def home_page():
    return render_template(template_name_or_list="home_page.html")
