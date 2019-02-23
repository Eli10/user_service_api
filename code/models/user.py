from db import db
import sqlite3
# from sqlalchemy.dialects import postgresql

class UserModel(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(80))
    icon = db.Column(db.String(80))
    preferences = db.Column(db.String())

    def __init__(self, username, password, location, icon, preferences):
        self.username = username
        self.password = password
        self.location = location
        self.icon = icon
        self.preferences = preferences

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def to_json(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "location": self.location,
            "icon": self.icon,
            "preferences": self.preferences
        }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, u_id):
        return cls.query.filter_by(user_id=u_id).first()
