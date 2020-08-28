from flask import Flask, render_template

from scripts.database import db
from scripts.admin_login import admin_login

app = Flask(__name__)
app.register_blueprint(admin_login, url_prefix="/admin")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.sqlite3'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)