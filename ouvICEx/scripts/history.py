from flask import Flask, Blueprint, render_template, request, flash
from scripts.database import posts, db

app_history = Blueprint("app_history", __name__, template_folder="templates")

def return_values(ref_dpt, author_dpt, context, situation):
    query = db.session.query(posts)
    if (ref_dpt != None):
        query = query.filter_by(ref_dep=ref_dpt)
    if (author_dpt != None):
        query = query.filter_by(author_dep=author_dpt)
    if (context != None):
        query = query.filter_by(context_t=context)
    if (situation != None):
        query = query.filter_by(situation_t=situation)
    return query

@app_history.route("/history", methods=["POST", "GET"])
def history():
    dict_ref = {}
    if request.method == "POST":
        ref_dpt = None
        author_dpt = None
        context = None
        situation = None
        if request.form["ref_dpt"] != "0":
            ref_dpt = request.form["ref_dpt"]
        if request.form["author_dpt"] != "0":
            author_dpt = request.form["author_dpt"]
        if request.form["context"] != "0":
            context = request.form["context"]
        if request.form["situation"] != "0":
            situation = request.form["situation"]

        values_db = return_values(ref_dpt, author_dpt, context, situation)
        return render_template("historico.html", values=values_db,
                ref=db.session.query(posts.ref_dep.distinct()),
                author=db.session.query(posts.author_dep.distinct()),
                context=db.session.query(posts.context_t.distinct()),
                situation=db.session.query(posts.situation_t.distinct()))
    else:
        return render_template("historico.html", values=posts.query.all(),
                ref=db.session.query(posts.ref_dep.distinct()),
                author=db.session.query(posts.author_dep.distinct()),
                context=db.session.query(posts.context_t.distinct()),
                situation=db.session.query(posts.situation_t.distinct()))
