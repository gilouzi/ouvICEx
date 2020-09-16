from flask import Flask, Blueprint, render_template, request, flash
from scripts.database import posts, db
import datetime

app_form = Blueprint("app_form", __name__, template_folder="templates")

@app_form.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        post = request.form["post"]
        date = datetime.date.today()
        author_dep = request.form["author_dep"]
        ref_dep = request.form["ref_dep"]
        context_t = request.form["context_t"]
        is_checked = request.form["is_checked"]
        if is_checked:
            name = request.form["name"]
        else:
            name = "anônimo"
        situation_t = False
        envio = posts(post, name, date, author_dep, ref_dep, context_t, situation_t)
        db.session.add(envio)
        db.session.commit()
        flash("Informações enviadas!")
        return render_template("form.html")
    else:
        return render_template("form.html")