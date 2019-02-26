from flask_restful import Resource, reqparse
from models.restaurant import RestaurantModel


class RestaurantList(Resource):

    def get(self):
        restaurants = RestaurantModel.get_all()
        if restaurants:
            return {'restaurants': [ restaurant.to_json() for restaurant in restaurants ]}, 200
        return {'message':'User not registered'}, 404


class Restaurant(Resource):

    def get(self, name):
        restaurant = RestaurantModel.find_by_name(name)

        if restaurant:
            return restaurant.to_json()
        return {'message': 'Restaurant not registered'}, 404


class RestaurantSearch(Resource):

    def get(self, name):
        restaurants = RestaurantModel.find_by_search_name(name)

        if restaurants:
            return {'restaurants': [restaurant.to_json() for restaurant in restaurants] }
        return {'message': 'Restaurant not registered'}, 404
