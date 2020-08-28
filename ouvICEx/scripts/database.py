from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
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

class admin(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.String(50))
    password = db.Column("password", db.String(50))

    def __init__(self, email, password):
        self.email = email
        self.password = password