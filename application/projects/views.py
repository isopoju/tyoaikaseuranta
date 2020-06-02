from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.projects.models import Project
from application.projects.forms import ProjectForm

@app.route("/projects", methods=["GET"])
def projects_index():
    return render_template('projects/list.html', projects = Project.query.all())

@app.route("/projects/new/")
@login_required
def projects_form():
    return render_template('projects/new.html', form = ProjectForm())

@app.route("/projects/modify/<project_id>", methods=["GET"])
@login_required
def projects_modify(project_id):
    project = Project.query.get(project_id)

    return render_template('projects/update.html', form = ProjectForm(), project = project)

@app.route("/projects/update/<project_id>", methods=["POST"])
@login_required
def projects_update(project_id):
    form = ProjectForm(request.form)

    project = Project.query.get(project_id)

    if not project:
        return redirect(url_for('project_index')) 

    project.name = form.name.data
    project.description = form.description.data
    project.start_date = form.start_date.data
    project.end_date = form.end_date.data
    project.run = form.run.data

    if not form.validate():
        return render_template('projects/update.html', form = form, project = project)

    if not form.validate_on_submit():
        error = "Tarkista alkamis- ja päättymispäivämäärät."
        return render_template('projects/update.html', form = form, project = project, error = error)

    db.session().commit()
  
    return redirect(url_for('projects_view', project_id=project.id))

@app.route("/projects/", methods=["POST"])
@login_required
def projects_create():
    form = ProjectForm(request.form)

    if not form.validate():
        return render_template('projects/new.html', form = form)

    if not form.validate_on_submit():
        error = "Tarkista alkamis- ja päättymispäivämäärät."
        return render_template('projects/new.html', form = form, error = error)

    new_project = Project(form.name.data)
    new_project.description = form.description.data
    new_project.start_date = form.start_date.data
    new_project.end_date = form.end_date.data
    new_project.run = form.run.data
    new_project.owner_id = current_user.id

    db.session().add(new_project)
    db.session().commit()
  
    return redirect(url_for('projects_index'))

@app.route("/projects/<project_id>/", methods=["GET"])
@login_required
def projects_view(project_id):
    return render_template('projects/view.html', project = Project.query.get(project_id))
