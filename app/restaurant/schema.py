from marshmallow import Schema, fields, post_load
from . import model


class RestaurantLocationSchema(Schema):
    address = fields.String()
    locality = fields.String()
    city = fields.String()
    latitude = fields.String()
    longitude = fields.String()
    zipcode = fields.String()

    @post_load()
    def make_object(self, data, **kwargs):
        return model.RestaurantLocation(**data)


class RestaurantSchema(Schema):
    id = fields.String()
    name = fields.String()
    location = fields.Nested(RestaurantLocationSchema())
    average_cost_for_two = fields.Float()
    price_range = fields.Float()
    currency = fields.String()
    menu_url = fields.String()

    @post_load()
    def make_object(self, data, **kwargs):
        return model.Restaurant(**data)

class RestaurantResponseSchema(Schema):
    restaurant = fields.Nested(RestaurantSchema)

class RestaurantFilterSchema(Schema):
    city_id = fields.String()
    category_id = fields.String()

    @post_load()
    def make_object(self, data, **kwargs):
        return model.RestaurantFilter(**data)


class SearchRestaurantResponseSchema(Schema):
    results_found = fields.Integer()
    results_start = fields.Integer()
    results_shown = fields.Integer()
    restaurants = fields.Nested(RestaurantResponseSchema, many=True)

    @post_load()
    def make_object(self, data, **kwargs):
        return model.SearchRestaurantResponse(**data)


restaurant_filter_schema = RestaurantFilterSchema()
restaurant_schema = RestaurantSchema()
search_restaurant_response = SearchRestaurantResponseSchema()