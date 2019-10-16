from marshmallow import Schema, fields, post_load, ValidationError
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


class RestaurantFilterSchema(Schema):
    cityId = fields.String(attribute="city_id")
    categoryId = fields.String(attribute="category_id")

    @post_load()
    def make_object(self, data, **kwargs):
        return model.RestaurantFilter(**data)


restaurant_filter_schema = RestaurantFilterSchema()
restaurant_schema = RestaurantSchema()
