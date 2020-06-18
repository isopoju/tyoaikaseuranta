from application import db
from application.models import Base
from application.auth.models import User
from application.workload.models import Workload

from flask_login import current_user
from sqlalchemy.sql import text

attends = db.Table('participation',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id', ondelete="CASCADE")),
    db.Column('account_id', db.Integer, db.ForeignKey('account.id', ondelete="CASCADE"))
)

class Project(Base):
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    running = db.Column(db.Boolean, nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    participants = db.relationship("User", secondary=attends, backref=db.backref("attending", lazy="dynamic"))
    workloads = db.relationship("Workload", cascade="all, delete", backref="workload")

    def __init__(self, name, description, start_date, end_date, running, owner_id):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.running = running
        self.owner_id = owner_id

    def get_owner_name(self):
        return User.query.get(self.owner_id).name

    def get_workloads(self):
        return Workload.query.filter_by(worker_id=current_user.id, project_id=self.id).order_by(Workload.date.desc()).all()

    @staticmethod
    def project_workloads(project_id):
        print('MODEL', project_id)
        stmt = text("SELECT Account.name, sum(Workload.hours) FROM Account"
                     " LEFT JOIN Workload ON Workload.worker_id = Account.id"
                     " WHERE Workload.project_id = :project_id"
                     " GROUP BY Account.id"
                     " ORDER BY Account.name").params(project_id=project_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "hours":row[1]})

        return response
