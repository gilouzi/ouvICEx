from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from scripts.history import return_request
from scripts.database import db, posts, users

app_admin = Blueprint("admin", __name__, template_folder='templates/')

@app_admin.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        pwd = request.form['pwd']

        found_user = users.query.filter_by(user=user, password=pwd).first()
        if found_user:
            session['user'] = user
            session['pwd'] = pwd
            flash("Bem vindo novamente, %s!" % (session['user']), "info")
            return redirect(url_for('.view'))
        else:
            flash("Usuário e/ou senha incorreto, tente novamente", "danger")
            return render_template('login.html')
    else:
        if 'user' in session:
            flash("Você já se encontra logado no sistema!", "info")
            return redirect(url_for('.view'))

    return render_template('login.html')

@app_admin.route('/logout')
def logout():
    if 'user' in session:
        flash("Logout feito com sucesso!", "success")

    session.pop('user', None)
    session.pop('pwd', None)
    return redirect(url_for(".login"))

@app_admin.route('/changeStatus/<int:pid>')
def changeStatus(pid):
    if 'user' in session:
        post = posts.query.get(pid)
        post.situation_t = 0 if post.situation_t == 1 else 1
        db.session.commit()
        flash("Atualização feita com sucesso", "success")
    else:
        flash("Você não possui permissão para realizar essa ação", "danger")

    return redirect(url_for(".view"))

@app_admin.route("/cleaning/admin")
def cleaning():

    render_template("history.html", values=posts.query.all(),
        ref=db.session.query(posts.ref_dep.distinct()),
        author=db.session.query(posts.author_dep.distinct()),
        context=db.session.query(posts.context_t.distinct()),
        situation=db.session.query(posts.situation_t.distinct()),
        num_values= posts.query.count())

    return redirect(url_for(".view"))

@app_admin.route('/admin', methods=["POST", "GET"])
def view():
    if 'user' in session:
        if request.method == "POST":
            values_db = return_request(request)

            return render_template("admin.html", values=values_db,
                ref=db.session.query(posts.ref_dep.distinct()),
                author=db.session.query(posts.author_dep.distinct()),
                context=db.session.query(posts.context_t.distinct()),
                situation=db.session.query(posts.situation_t.distinct()),
                num_values= values_db.count())
        else:
            return render_template("admin.html", values=posts.query.all(),
                    ref=db.session.query(posts.ref_dep.distinct()),
                    author=db.session.query(posts.author_dep.distinct()),
                    context=db.session.query(posts.context_t.distinct()),
                    situation=db.session.query(posts.situation_t.distinct()),
                    num_values= posts.query.count())

    return redirect(url_for(".login"))
