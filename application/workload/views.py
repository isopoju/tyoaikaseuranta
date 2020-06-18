from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.workload.models import Workload
from application.workload.forms import WorkloadForm

@app.route("/workloads/modify/<workload_id>", methods=["GET"])
@login_required(role="ADMIN")
@login_required
def workloads_modify(workload_id):
    workload = Workload.query.get(workload_id)
    if not workload:
        return redirect(url_for('projects_index'))

    return render_template('workload/update.html', form = WorkloadForm(), workload = workload)

@app.route("/workloads/update/<workload_id>", methods=["POST"])
@login_required
def workloads_update(workload_id):
    form = WorkloadForm(request.form)

    workload = Workload.query.get(workload_id)
    if workload.worker_id != current_user.id:
        return redirect(url_for('projects_index'))

    # if not workload:
    #     return redirect(url_for('projects_index'))

    workload.date = form.date.data
    workload.hours = form.hours.data
    workload.task = form.task.data

    if not form.validate():
        return render_template('workload/update.html', form = form, workload = workload)

    db.session().commit()

    return redirect(url_for('projects_view', project_id=workload.project_id))

@app.route("/workloads/delete/<workload_id>/", methods=["POST"])
@login_required(role="ADMIN")
def workloads_delete(workload_id):
    deleted_workload = Workload.query.get(workload_id)
    if deleted_workload.worker_id != current_user.id:
        return redirect(url_for('projects_index'))

    db.session().delete(deleted_workload)
    db.session().commit()

    return redirect(url_for('projects_view', project_id=deleted_workload.project_id))

@app.route("/workloads/report/", methods=["GET"])
@login_required(role="ADMIN")
def workload_report():
    return render_template("workload/report.html")