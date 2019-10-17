from marshmallow import Schema, fields, post_load
from . import model


class CategorySchema(Schema):
    id = fields.Integer()
    name = fields.String()
    zomato_ids = fields.List(fields.Integer)

    @post_load()
    def make_object(self, data, **kwargs):
        return model.Category(**data)


category_schema = CategorySchema()
