from flask_restful import Resource, reqparse
from models.restaurant import RestaurantModel


class RestaurantList(Resource):

    def get(self):
        restaurants = RestaurantModel.get_all()
        if restaurants:
            return {'restaurants': [ restaurant.to_json() for restaurant in restaurants ]}, 200
        return {'message':'User not registered'}, 404
