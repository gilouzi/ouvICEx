from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.sqlite3'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)

class posts(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    post = db.Column("post", db.String(500))
    date = db.Column("date", db.Date)
    author_dep = db.Column("author_dep", db.String(50))
    ref_dep = db.Column("ref_dep", db.String(50))
    context_t = db.Column("context_t", db.String(20))
    situation_t = db.Column("situation_t", db.String(20))

    def __init__(self, post, date, author_dep, ref_dep, context_t, situation_t):
        self.post = post
        self.date = date
        self.author_dep = author_dep
        self.ref_dep = ref_dep
        self.context_t = context_t
        self.situation_t = situation_t

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/historico", methods=["POST", "GET"])
def historico():
    if request.method == "POST":
        if request.form["dpt"]:
            dpt = request.form["dpt"]
            return render_template("historico.html", values=posts.query.filter_by(ref_dep=dpt))

        elif request.form["limpar"]:
            return render_template("historico.html", values=posts.query.all())
    else:
        return render_template("historico.html", values=posts.query.all())


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

if __name__ == "__main__":
    db.create_all()

    app.run(debug=True)
