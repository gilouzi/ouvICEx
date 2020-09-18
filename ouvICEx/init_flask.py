from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from scripts import analyses as anl
from scripts.admin import app_admin
from scripts.history import app_history
from scripts.form import app_form
from scripts.analyses import app_analyses
from scripts.database import db, posts, users

app = Flask(__name__)
app.register_blueprint(app_admin, url_prefix="/admin")
app.register_blueprint(app_history, url_prefix="")
app.register_blueprint(app_form, url_prefix="")
app.register_blueprint(app_analyses, url_prefix="")
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.sqlite3'

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/view")
def view():
    return render_template("view.html", values = posts.query.all())

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
    with app.app_context():
        db.create_all()

        # Criando usuário padrão para testes
        default_user = users.query.filter_by(user="DefaultUser").first()
        if default_user == None:
            usr = users("DefaultUser", "1234")
            db.session.add(usr)
            db.session.commit()

    app.run(debug=True)
