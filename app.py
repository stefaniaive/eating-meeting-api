from restaurant.resource import RestaurantCollectionResource, RestaurantEntityResource
from flask import Blueprint
from flask_restful import Api
from config import APP_NAME

api_bp = Blueprint(APP_NAME, __name__)
api = Api(api_bp)

# Route
api.add_resource(RestaurantCollectionResource, '/restaurants')
api.add_resource(RestaurantEntityResource, '/restaurants/<id>')
