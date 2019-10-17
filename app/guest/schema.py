from marshmallow import Schema, fields, post_load
from . import model


class GuestSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.String()

    @post_load()
    def make_object(self, data):
        return model.Guest(**data)


guest_schema = GuestSchema()
