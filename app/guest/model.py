from db.postgress_connector import db


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.first_name = kwargs.get("first_name", None)
        self.last_name = kwargs.get("last_name", None)
        self.email = kwargs.get("email", None)

class GuestInput(object):
    id = None
    first_name = None
    last_name = None
    email = None

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.first_name = kwargs.get("first_name", None)
        self.last_name = kwargs.get("last_name", None)
        self.email = kwargs.get("email", None)