from db.postgress_connector import db
from sqlalchemy import types
from sqlalchemy.orm import relationship
from app.guest.model import Guest
from sqlalchemy import ForeignKey


class MeetingGuest(db.Model):
    __tablename__ = 'meeting_guest'

    guest_id = db.Column(db.Integer, ForeignKey('guest.id'), primary_key=True)
    meeting_id = db.Column(db.Integer, ForeignKey('meeting.id'), primary_key=True)


class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.String, nullable=False)
    date = db.Column(types.DateTime, nullable=False)
    guests = relationship(Guest, uselist=True, secondary='meeting_guest', cascade="save-update")

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.restaurant_id = kwargs.get("restaurant_id", None)
        self.date = kwargs.get("date", None)
        self.guests = kwargs.get("guests", None)


class MeetingInput(object):
    id = None
    restaurant_id = None
    date = None
    guests = None

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.restaurant_id = kwargs.get("restaurant_id", None)
        self.date = kwargs.get("date", None)
        self.guests = kwargs.get("guests", None)
