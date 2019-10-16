from flask import request, make_response
from flask_restful import Resource
from .service import restaurant_service
from restaurant.schema import restaurant_schema

class RestaurantCollectionResource(Resource):
    pass

class RestaurantEntityResource(Resource):

    def get(self, id):
        restaurant = restaurant_service.get_restaurant(id)

        response = make_response(restaurant_schema.dumps(restaurant).data, 200)

        return response