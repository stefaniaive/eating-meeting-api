import config
import requests
from restaurant.schema import restaurant_schema
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

zomato_client = ZomatoClient(config.ZOMATO_URL, config.ZOMATO_API_KEY)

