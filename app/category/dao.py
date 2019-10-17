from .model import Category

class CategoryDAO(object):

    def retrieve_all(self):
        return Category.query.all()

    def retrieve(self, category_id):
        return Category.query.filter(Category.id==category_id).one_or_none()

category_dao =  CategoryDAO()