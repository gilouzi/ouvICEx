from flask import Flask, render_template

from scripts.database import db, users
from scripts.admin import admin

app = Flask(__name__)
app.secret_key = 'secrey_key'

app.register_blueprint(admin, url_prefix="/admin")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.sqlite3'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

@app.route("/")
def home():
    return render_template("home.html")


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