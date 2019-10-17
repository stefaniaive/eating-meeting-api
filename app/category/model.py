from db.postgress_connector import db
from sqlalchemy.types import ARRAY

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    zomato_ids = db.Column(ARRAY(db.Integer))

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.name = kwargs.get("name", None)
        self.zomato_ids = kwargs.get("zomato_ids", None)

