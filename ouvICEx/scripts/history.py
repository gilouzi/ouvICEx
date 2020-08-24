from flask import Flask, Blueprint, render_template, request, flash
from scripts.database import posts

app_history = Blueprint("app_history", __name__, template_folder="templates")

@app_history.route("/history", methods=["POST", "GET"])
def history():
    if request.method == "POST":
        if request.form["refdpt"] == "0" and request.form["author_dpt"] == "0":
            return render_template("historico.html", values=posts.query.all())
        elif request.form["author_dpt"] == "0":
            ref_dpt = request.form["ref_dpt"]
            return render_template("historico.html", values=posts.query.filter_by(ref_dep=ref_dpt))
        elif request.form["dpt"] == "0":
            author_dpt = request.form["author_dpt"]
            return render_template("historico.html", values=posts.query.filter_by(author_dep=author_dpt))
        else:
            ref_dpt = request.form["ref_dpt"]
            author_dpt = request.form["dpt_author"]
            return render_template("historico.html", values=posts.query.filter_by(author_dep=author_dpt, ref_dep=ref_dpt))
    else:
        return render_template("historico.html", values=posts.query.all())
