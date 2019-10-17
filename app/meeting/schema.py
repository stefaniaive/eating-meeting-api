from marshmallow import Schema, fields, post_load
from . import model
from app.guest.schema import GuestSchema


class MeetingSchema(Schema):
    id = fields.Integer()
    restaurant_id = fields.Integer()
    date = fields.DateTime()
    guests = fields.Nested(GuestSchema, many=True)

    @post_load()
    def make_object(self, data):
        return model.Meeting(**data)


meeting_schema = MeetingSchema()
