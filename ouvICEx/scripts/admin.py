from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from scripts.database import admin

admin = Blueprint("admin", __name__, template_folder='templates/')

@admin.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['email'] = request.form["email"]
        session['pwd'] = request.form["pwd"]
        return redirect(url_for('admin.view'))
    else:
        if 'email' in session:
            return redirect(url_for('admin.view'))

    return render_template('admin_login.html')

@admin.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('pwd', None)
    return redirect(url_for("home"))

@admin.route('/')
@admin.route('/view')
def view():
    if 'email' in session:
        return render_template('admin_view.html')
    else:
        return redirect(url_for("admin.login"))