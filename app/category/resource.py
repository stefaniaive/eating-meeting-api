from flask_restful import Resource
import json
from .schema import category_schema
from .dao import category_dao

class CategoryCollectionResource(Resource):

    def get(self):
        # TODO: Pagination
        categories = category_dao.retrieve_all()
        return json.loads(category_schema.dumps(categories, many=True).data)
