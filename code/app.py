from flask import Flask
from flask_restful import Api
import os
from db import db

from resources.user import UserRegister


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
api = Api(app)


api.add_resource(UserRegister, '/user')


@app.before_first_request
def create_tables():
    db.create_all()

db.init_app(app)
app.run(port=5000, debug=True)
