from db import db
import sqlite3
# from sqlalchemy.dialects import postgresql

class RestaurantModel(db.Model):

    __tablename__ = "restaurants"

    restaurant_id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    tags = db.Column(db.String(80))
    lat = db.Column(db.Float(6), nullable=False)
    lon = db.Column(db.Float(6), nullable=False)

    def __init__(self, restaurant_name, address, tags, lat, lon):
        self.restaurant_name = restaurant_name
        self.address = address
        self.tags = tags
        self.lat = lat
        self.lon = lon

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def to_json(self):
        return {
            "restaurant_id": self.restaurant_id,
            "restaurant_name": self.restaurant_name,
            "address": self.address,
            "tags": self.tags,
            "lat": self.lat,
            "lon": self.lon
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(restaurant_name=name).first()

    @classmethod
    def find_by_id(cls, u_id):
        return cls.query.filter_by(restaurant_id=u_id).first()
