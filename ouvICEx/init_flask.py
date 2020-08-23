from flask import Flask, render_template

from database.posts import db
from admin.posts import admin_view

app = Flask(__name__)
app.register_blueprint(admin_view, url_prefix="/admin")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.sqlite3'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)