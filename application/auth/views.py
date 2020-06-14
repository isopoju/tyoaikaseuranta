from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    if not form.validate():
        # validoidaan liian pitkat kentat => sivu ei kaadu
        error = "Väärä käyttäjätunnus tai salasana."
        return render_template("auth/loginform.html", form = form, error=error)

    user = User.query.filter_by(username=form.username.data).first()
    if not (user and check_password_hash(user.password, form.password.data)):
        error = "Väärä käyttäjätunnus tai salasana."
        return render_template("auth/loginform.html", form = form, error = error)

    login_user(user)
    return redirect(url_for("projects_index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET"])
def register_form():
    return render_template("auth/registerform.html", form = RegisterForm())

@app.route("/auth/register", methods = ["POST"])
def register():
    form = RegisterForm(request.form)
    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    user = User.query.filter_by(username = form.username.data).first()
    if user:
        form.username.errors.append("Käyttäjätunnus on jo käytössä")
        return render_template("auth/registerform.html", form = form)

    new_user = User(form.name.data, form.email.data, form.username.data, form.password.data, False)

    db.session().add(new_user)
    db.session().commit()

    login_user(new_user)
    return redirect(url_for("projects_index"))