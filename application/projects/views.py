from flask import redirect, render_template, request, url_for

from application import app, db
from application.projects.models import Project
from application.projects.forms import ProjectForm

@app.route("/projects", methods=["GET"])
def projects_index():
    return render_template("projects/list.html", projects = Project.query.all())

@app.route("/projects/new/")
def projects_form():
    return render_template("projects/new.html", form = ProjectForm())
  
@app.route("/projects/<project_id>/", methods=["POST"])
def projects_set_ended(project_id):

    p = Project.query.get(project_id)
    p.ended = True
    db.session().commit()
  
    return redirect(url_for("projects_index"))

@app.route("/projects/", methods=["POST"])
def projects_create():
    form = ProjectForm(request.form)

    p = Project(form.name.data)
    p.ended = form.ended.data

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("projects_index"))