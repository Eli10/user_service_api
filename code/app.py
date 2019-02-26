from flask import Flask
from flask_restful import Api
import os
from db import db

from resources.user import UserRegister, User
from resources.restaurant import RestaurantList, RestaurantSearch, Restaurant

from insert_restaurants import insert_restaurants

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
api = Api(app)


api.add_resource(UserRegister, '/user/register')
api.add_resource(User, '/user/<string:name>')
api.add_resource(RestaurantList, '/restaurants')
api.add_resource(Restaurant, '/restaurant/<string:name>')
api.add_resource(RestaurantSearch, '/restaurant/search/<string:name>')

@app.before_first_request
def create_tables():
    db.create_all()
    insert_restaurants()

db.init_app(app)
app.run(port=5000, debug=True)
