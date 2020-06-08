from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_manager, login_required
from application.projects.models import Project
from application.projects.forms import ProjectForm
from application.auth.models import User
from application.workload.models import Workload
from application.workload.forms import WorkloadForm

@app.route("/projects", methods=["GET"])
def projects_index():
    return render_template('projects/list.html', projects = Project.query.all())

@app.route("/projects/new/", methods=["GET"])
@login_required(role="ADMIN")
def projects_form():
    return render_template('projects/new.html', form = ProjectForm())

@app.route("/projects/modify/<project_id>", methods=["GET"])
@login_required(role="ADMIN")
@login_required
def projects_modify(project_id):
    project = Project.query.get(project_id)
    if not project:
        return redirect(url_for('projects_index'))

    return render_template('projects/update.html', form = ProjectForm(), project = project)

@app.route("/projects/update/<project_id>", methods=["POST"])
@login_required
def projects_update(project_id):
    form = ProjectForm(request.form)

    project = Project.query.get(project_id)
    if project.owner_id != current_user.id:
        return redirect(url_for('projects_index'))

    if not project:
        return redirect(url_for('projects_index'))

    project.name = form.name.data
    project.description = form.description.data
    project.start_date = form.start_date.data
    project.end_date = form.end_date.data
    project.running = form.running.data

    if not form.validate():
        return render_template('projects/update.html', form = form, project = project)

    if not form.validate_dates():
        form.end_date.errors.append("Päättyy ennen alkamista")
        return render_template('projects/update.html', form = form, project = project)

    db.session().commit()

    return redirect(url_for('projects_view', project_id=project.id))

@app.route("/projects/", methods=["POST"])
@login_required(role="ADMIN")
def projects_create():
    form = ProjectForm(request.form)

    if not form.validate():
        return render_template('projects/new.html', form = form)

    if not form.validate_dates():
        form.end_date.errors.append("Päättyy ennen alkamista")
        return render_template('projects/new.html', form = form)

    new_project = Project(
        form.name.data,
        form.description.data,
        form.start_date.data,
        form.end_date.data,
        form.running.data,
        current_user.id
    )

    db.session().add(new_project)
    db.session().commit()

    return redirect(url_for('projects_index'))

@app.route("/projects/<project_id>/", methods=["GET"])
@login_required(role="ADMIN")
def projects_view(project_id):
    if not Project.query.get(project_id):
        return redirect(url_for('projects_index'))

    return render_template('projects/view.html', project = Project.query.get(project_id), form = WorkloadForm())

@app.route("/projects/delete/<project_id>/", methods=["POST"])
@login_required(role="ADMIN")
def projects_delete(project_id):
    deleted_project = Project.query.get(project_id)

    # tahan ehka popup varmistus..

    db.session().delete(deleted_project)
    db.session().commit()

    return redirect(url_for('projects_index'))

@app.route("/projects/join/<project_id>/", methods=["POST"])
@login_required(role="ADMIN")
def projects_join(project_id):
    project = Project.query.get(project_id)
    logged_user = User.query.get(current_user.id)

    if not project in logged_user.attending:
        project.participants.append(logged_user)

        db.session().add(project)
        db.session().commit()

    return redirect(url_for('projects_view', project_id=project.id))

@app.route("/projects/<project_id>", methods=["POST"])
@login_required(role="ADMIN")
def workloads_create(project_id):
    project = Project.query.get(project_id)
    if not project:
        return redirect(url_for('projects_index'))

    form = WorkloadForm(request.form)
    if not form.validate():
        return render_template('projects/view.html', project = project, form = form)

    new_workload = Workload(
        form.date.data,
        form.hours.data,
        form.task.data,
        current_user.id,
        project_id
    )

    db.session().add(new_workload)
    db.session().commit()

    return redirect(url_for('projects_view', project_id=project.id))

@app.route("/project/hourly_report/<project_id>", methods=["GET"])
@login_required(role="ADMIN")
def projects_hourly_report(project_id):

    return render_template("projects/hourly_report.html", project_id = project_id)