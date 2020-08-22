from flask import Flask, Blueprint, render_template

b_posts = Blueprint("b_posts", __name__, static_folder="static", template_folder="templates")

@b_posts.route("/posts")
def posts():
    return render_template("posts.html")