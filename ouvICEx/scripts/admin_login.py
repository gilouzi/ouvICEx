from flask import Blueprint, render_template, flash

admin_login = Blueprint("admin_login", __name__, template_folder='templates/')

@admin_login.route('/login')
def login():
    return render_template('admin_login.html')