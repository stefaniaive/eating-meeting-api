from zomato.client import zomato_client

class RestaurantService(object):

    def get_restaurant(self, id):
        return zomato_client.retrieve_restaurant(id)


restaurant_service = RestaurantService()