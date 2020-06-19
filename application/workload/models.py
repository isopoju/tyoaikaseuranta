from application import db
from application.models import Base

from sqlalchemy.sql import text

class Workload(Base):
    date = db.Column(db.Date, nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    task = db.Column(db.String(128), nullable=False)

    worker_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    def __init__(self, date, hours, task, worker_id, project_id):
        self.date = date
        self.hours = hours
        self.task = task
        self.worker_id = worker_id
        self.project_id = project_id

    @staticmethod
    def user_workloads(account_id):
        stmt = text("SELECT Project.id, Project.name, sum(Workload.hours) FROM Project"
                     " LEFT JOIN Workload ON Workload.project_id = Project.id"
                     " WHERE Workload.worker_id = :account_id"
                     " GROUP BY Project.id"
                     " ORDER BY Project.name").params(account_id=account_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name":row[1], "hours":row[2]})

        return response
