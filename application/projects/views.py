from application import app, db
from flask import redirect, render_template, request, url_for
from application.projects.models import Project

@app.route("/projects", methods=["GET"])
def projects_index():
    return render_template("projects/list.html", projects = Project.query.all())

@app.route("/projects/new/")
def projects_form():
    return render_template("projects/new.html")
  
@app.route("/projects/<project_id>/", methods=["POST"])
def projects_set_done(project_id):

    t = Project.query.get(project_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("projects_index"))

@app.route("/projects/", methods=["POST"])
def projects_create():
    t = Project(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("projects_index"))