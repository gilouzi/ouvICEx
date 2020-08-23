from flask import Flask, Blueprint, render_template
from database.posts import posts

admin_view = Blueprint("admin_view", __name__, static_folder="static", template_folder="templates")

@admin_view.route("/view")
def view():
    return render_template("view.html", posts=posts.query.all())