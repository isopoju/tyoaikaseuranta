from application import db
from application.models import Base

from flask_login import current_user
from werkzeug.security import generate_password_hash

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(16), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    remember = db.Column(db.Boolean, nullable=False)

    projects = db.relationship("Project", backref="account", lazy=True)
    workloads = db.relationship("Workload", backref='account', lazy=True)

    def __init__(self, name, email, username, password, remember):
        self.name = name
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.remember = remember

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if current_user.username == 'admin':
            return ["ADMIN"]
        return []