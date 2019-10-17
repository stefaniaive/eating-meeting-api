from .dao import category_dao


class CategoryMapper(object):

    def get_zomato_categories_as_filter(self, category_id):
        category = category_dao.retrieve(category_id)
        categories_as_filter = ",".join(str(x) for x in category.zomato_ids)

        return categories_as_filter


category_mapper = CategoryMapper()