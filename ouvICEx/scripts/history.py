from flask import Flask, Blueprint, render_template, request, flash
from scripts.database import posts, db

app_history = Blueprint("app_history", __name__, template_folder="templates")

@app_history.route("/history", methods=["POST", "GET"])
def history():
    if request.method == "POST":
        if request.form["context"] == "0":
            if request.form["ref_dpt"] == "0" and request.form["author_dpt"] == "0":
                return render_template("historico.html", values=posts.query.all(),
                        ref=db.session.query(posts.ref_dep.distinct()), author=db.session.query(posts.author_dep.distinct()),
                        context=db.session.query(posts.context_t.distinct()))

            elif request.form["author_dpt"] == "0":
                ref_dpt = request.form["ref_dpt"]
                return render_template("historico.html", values=posts.query.filter_by(ref_dep=ref_dpt),
                        ref=db.session.query(posts.ref_dep.distinct()), author=db.session.query(posts.author_dep.distinct()),
                        context=db.session.query(posts.context_t.distinct()))

            elif request.form["ref_dpt"] == "0":
                author_dpt = request.form["author_dpt"]
                return render_template("historico.html", values=posts.query.filter_by(author_dep=author_dpt),
                        ref=db.session.query(posts.ref_dep.distinct()), author=db.session.query(posts.author_dep.distinct()),
                        context=db.session.query(posts.context_t.distinct()))
            else:
                ref_dpt = request.form["ref_dpt"]
                author_dpt = request.form["author_dpt"]
                return render_template("historico.html", values=posts.query.filter_by(author_dep=author_dpt, ref_dep=ref_dpt),
                        ref=db.session.query(posts.ref_dep.distinct()), author=db.session.query(posts.author_dep.distinct()),
                        context=db.session.query(posts.context_t.distinct()))
        else:
            cont = request.form["context"]
            if request.form["ref_dpt"] == "0" and request.form["author_dpt"] == "0":
                return render_template("historico.html", values=posts.query.filter_by(context_t=cont),
                        ref=db.session.query(posts.ref_dep.distinct()), author=db.session.query(posts.author_dep.distinct()),
                        context=db.session.query(posts.context_t.distinct()))

            elif request.form["author_dpt"] == "0":
                ref_dpt = request.form["ref_dpt"]
                return render_template("historico.html", values=posts.query.filter_by(ref_dep=ref_dpt, context_t=cont),
                        ref=db.session.query(posts.ref_dep.distinct()), author=db.session.query(posts.author_dep.distinct()),
                        context=db.session.query(posts.context_t.distinct()))

            elif request.form["ref_dpt"] == "0":
                author_dpt = request.form["author_dpt"]
                return render_template("historico.html", values=posts.query.filter_by(author_dep=author_dpt, context_t=cont),
                        ref=db.session.query(posts.ref_dep.distinct()), author=db.session.query(posts.author_dep.distinct()),
                        context=db.session.query(posts.context_t.distinct()))
            else:
                ref_dpt = request.form["ref_dpt"]
                author_dpt = request.form["author_dpt"]
                return render_template("historico.html", values=posts.query.filter_by(author_dep=author_dpt, ref_dep=ref_dpt, context_t=cont),
                        ref=db.session.query(posts.ref_dep.distinct()), author=db.session.query(posts.author_dep.distinct()),
                        context=db.session.query(posts.context_t.distinct()))
    else:
        return render_template("historico.html", values=posts.query.all(),
                ref=db.session.query(posts.ref_dep.distinct()), author=db.session.query(posts.author_dep.distinct()),
                context=db.session.query(posts.context_t.distinct()))
