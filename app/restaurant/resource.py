from flask import request
from flask_restful import Resource
from .service import restaurant_service
from app.restaurant.schema import restaurant_schema, restaurant_filter_schema, search_restaurant_response
import json


class RestaurantCollectionResource(Resource):

    def get(self):
        # TODO: Pagination
        city_id = request.args.get('city_id', None)
        category_id = request.args.get('category_id', None)
        filter_payload = json.dumps({"category_id": category_id, "city_id": city_id})
        filter = restaurant_filter_schema.loads(filter_payload).data

        search_response = restaurant_service.get_restaurants(filter)
        return json.loads(search_restaurant_response.dumps(search_response).data)


class RestaurantEntityResource(Resource):

    def get(self, id):
        restaurant = restaurant_service.get_restaurant(id)
        return json.loads(restaurant_schema.dumps(restaurant).data)