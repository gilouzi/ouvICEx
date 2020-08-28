from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from scripts.database import users

admin = Blueprint("admin", __name__, template_folder='templates/')

@admin.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        pwd = request.form['pwd']
        found_user = users.query.filter_by(user=user, password=pwd).first()
        if found_user:
            session['user'] = user
            session['pwd'] = pwd
            return redirect(url_for('admin.view'))
        else:
            flash("Usuário e/ou senha incorreto, tente novamente")
            return render_template('admin_login.html')
    else:
        if 'user' in session:
            return redirect(url_for('admin.view'))

    return render_template('admin_login.html')

@admin.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('pwd', None)
    return redirect(url_for("home"))

@admin.route('/')
@admin.route('/view')
def view():
    if 'user' in session:
        return render_template('admin_view.html')
    
    return redirect(url_for("admin.login"))