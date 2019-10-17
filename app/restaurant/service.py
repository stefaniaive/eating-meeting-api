from app.zomato.client import zomato_client
from app.category.mapper import category_mapper

class RestaurantService(object):

    def get_restaurant(self, id):
        return zomato_client.retrieve_restaurant(id)

    def get_restaurants(self, filter):
        category_ids = category_mapper.get_zomato_categories_as_filter(filter.category_id)
        return zomato_client.retrieve_restaurants(filter.city_id, category_ids)


restaurant_service = RestaurantService()