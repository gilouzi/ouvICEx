from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from admin.posts import b_posts

app = Flask(__name__)
app.register_blueprint(b_posts, url_prefix="/admin")
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


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)