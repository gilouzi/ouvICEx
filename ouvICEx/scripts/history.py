from flask import Flask, Blueprint, redirect, url_for, render_template, request, flash
from scripts.database import posts, db
from sqlalchemy import Date, func
import datetime

app_history = Blueprint("app_history", __name__, template_folder="templates")

def db_filters(ref_dpt, author_dpt, context, situation, date_start, date_end):

    if (date_start != None and date_end != None):
        query = db.session.query(posts).filter(posts.date>=date_start, posts.date<=date_end)
    elif (date_start != None):
        query = db.session.query(posts).filter(posts.date>=date_start, posts.date<=datetime.date.today())
    elif (date_end != None):
        query = db.session.query(posts).filter(posts.date<=date_end)
    else:
        query = db.session.query(posts)

    if (ref_dpt != None):
        query = query.filter(posts.ref_dep==ref_dpt)
    if (author_dpt != None):
        query = query.filter(posts.author_dep==author_dpt)
    if (context != None):
        query = query.filter(posts.context_t==context)
    if (situation != None):
        query = query.filter(posts.situation_t==situation)

    return query

def return_request(request):
    ref_dpt = None
    author_dpt = None
    context = None
    situation = None
    date_start = None
    date_end = None
    if request.form["ref_dpt"] != "0":
        ref_dpt = request.form["ref_dpt"]
    if request.form["author_dpt"] != "0":
        author_dpt = request.form["author_dpt"]
    if request.form["context"] != "0":
        context = request.form["context"]
    if request.form["situation"] != "-1":
        situation = request.form["situation"]
    if request.form["start"]:
        date_start = request.form["start"]
    if request.form["end"]:
        date_end = request.form["end"]

    return db_filters(ref_dpt, author_dpt, context, situation, date_start, date_end)


@app_history.route("/cleaning/history")
def cleaning():

    render_template("history.html", values=posts.query.all(),
        ref=db.session.query(posts.ref_dep.distinct()),
        author=db.session.query(posts.author_dep.distinct()),
        context=db.session.query(posts.context_t.distinct()),
        situation=db.session.query(posts.situation_t.distinct()),
        num_values= posts.query.count())

    return redirect(url_for("app_history.history"))

@app_history.route("/history", methods=["POST", "GET"])
def history():

    if request.method == "POST":
        values_db = return_request(request)

        return render_template("history.html", values=values_db,
                ref=db.session.query(posts.ref_dep.distinct()),
                author=db.session.query(posts.author_dep.distinct()),
                context=db.session.query(posts.context_t.distinct()),
                situation=db.session.query(posts.situation_t.distinct()),
                num_values= values_db.count())
    else:
        return render_template("history.html", values=posts.query.all(),
                ref=db.session.query(posts.ref_dep.distinct()),
                author=db.session.query(posts.author_dep.distinct()),
                context=db.session.query(posts.context_t.distinct()),
                situation=db.session.query(posts.situation_t.distinct()),
                num_values= posts.query.count())
