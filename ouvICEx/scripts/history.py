from flask import Flask, Blueprint, render_template, request, flash
from scripts.database import posts

app_history = Blueprint("app_history", __name__, template_folder="templates")

@app_history.route("/history", methods=["POST", "GET"])
def history():
    if request.method == "POST":
        if request.form["dpt"]:
            dpt = request.form["dpt"]
            return render_template("historico.html", values=posts.query.filter_by(ref_dep=dpt))

        elif request.form["limpar"]:
            return render_template("historico.html", values=posts.query.all())
    else:
        print("ola")
        return render_template("historico.html")
