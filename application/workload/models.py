from application import db
from application.models import Base

class Workload(Base):
    date = db.Column(db.Date, nullable=False)
    hours = db.Column(db.Float, nullable=False)
    task = db.Column(db.String(128), nullable=False)

    worker_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    def __init__(self, date, hours, task, worker_id, project_id):
        self.date = date
        self.hours = hours
        self.task = task
        self.worker_id = worker_id
        self.project_id = project_id