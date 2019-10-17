from db.postgress_connector import db
from sqlalchemy import types
from sqlalchemy.orm import relationship
from app.guest.model import Guest

meeting_guest = db.Table('meeting_guest', db.Base.metadata,
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('meeting_id', db.Integer, db.ForeignKey('meeting.id'))
)

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, nullable=False)
    date = db.Column(types.DateTime, nullable=False)
    guests = relationship(Guest, uselist=True, secondary=meeting_guest)

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.restaurant_id = kwargs.get("restaurant_id", None)
        self.date = kwargs.get("date", None)
        self.guests = kwargs.get("guests", None)


