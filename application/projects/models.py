from application import db
from application.models import Base
from application.auth.models import User

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