import config
from app.restaurant.schema import restaurant_schema, search_restaurant_response
import requests
import json

class ZomatoClient(object):

    def __init__(self, url, key):
        self.url = url
        self.key = key

    def _get_headers(self):
        return {config.ZOMATO_AUTHENTICATION_HEADER: self.key}

    def retrieve_restaurant(self, id):
        try:
                response = requests.get(
                    self.url + '/restaurant?res_id= %s' % id,
                    headers= self._get_headers()
                )
                
                entity_response = json.loads(response.text)

                return restaurant_schema.load(entity_response).data

        except Exception as e:
            print('Error retrieving Restaurant by Id {}'.format(id, e.message))
            raise e

    def retrieve_restaurants(self, city_id, category_ids):
        search_url = self.url + '/search?entity_id=%s&entity_type=city&category=%s' % (city_id, category_ids)
        try:
            response = requests.get(
                search_url,
                headers= self._get_headers()
            )

            entity_response = json.loads(response.text)
            return search_restaurant_response.load(entity_response).data

        except Exception as e:
            print('Error retrieving Restaurant by Id {}'.format(id, e.message))
            raise e


zomato_client = ZomatoClient(config.ZOMATO_URL, config.ZOMATO_API_KEY)

