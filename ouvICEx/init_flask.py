from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import datetime
from scripts import analyses as anl
from scripts.history import app_history
from scripts.database import db, posts

app = Flask(__name__)
app.register_blueprint(app_history, url_prefix="")
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.sqlite3'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/view")
def view():
    return render_template("view.html", values = posts.query.all())

@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        post = request.form["post"]
        date = datetime.date.today()
        author_dep = request.form["author_dep"]
        ref_dep = request.form["ref_dep"]
        context_t = request.form["context_t"]
        situation_t = request.form["situation_t"]
        envio = posts(post, date, author_dep, ref_dep, context_t, situation_t)
        db.session.add(envio)
        db.session.commit()
        #flash("Informações enviadas!")
        return render_template("form.html")
    else:
        return render_template("form.html")

@app.route("/analyses", methods=["POST", "GET"])
def analyses():
    #print("entrou")
    #anl.test()
    #return "analyses content"
    if request.method == "GET":
        return render_template(
                    "analyses.html",
                    values = posts.query.all()
                )
    else:
        return "ERROR"

if __name__ == "__main__":

    db.init_app(app)
    app.run(debug=True)
