"""
{
  "id": "16774318",
  "name": "Otto Enoteca & Pizzeria",
  "url": "https://www.zomato.com/new-york-city/otto-enoteca-pizzeria-greenwich-village",
  "location": {
    "address": "1 5th Avenue, New York, NY 10003",
    "locality": "Greenwich Village",
    "city": "New York City",
    "latitude": "40.732013",
    "longitude": "-73.996155",
    "zipcode": "10003",
    "country_id": "216"
  },
  "average_cost_for_two": "60",
  "price_range": "2",
  "currency": "$"
"""


class RestaurantLocation(object):

    address = None
    locality = None
    city= None
    latitude = None
    longitude = None
    zipcode = None

    def __init__(self, **kwargs):
        self.address = kwargs.get("address", None)
        self.locality = kwargs.get("locality", None)
        self.city = kwargs.get("city", None)
        self.latitude = kwargs.get("latitude", None)
        self.longitude = kwargs.get("longitude", None)
        self.zipcode = kwargs.get("zipcode", None)


class Restaurant(object):

    id = None
    name = None
    location = None
    average_cost_for_two = None
    price_range = None
    currency = None
    menu_url = None

    def __init__(self, **kwargs):
        self.id = kwargs.get("id",None)
        self.name = kwargs.get("name",None)
        self.location = kwargs.get("location",None)
        self.average_cost_for_two = kwargs.get("average_cost_for_two",None)
        self.price_range = kwargs.get("price_range",None)
        self.currency = kwargs.get("currency",None)
        self.menu_url = kwargs.get("menu_url",None)


class RestaurantFilter(object):

    city_id = None
    category_id = None

    def __init__(self, **kwargs):
        self.city_id = kwargs.get("city_id",None)
        self.category_id = kwargs.get("category_id",None)


class SearchRestaurantResponse(object):

    results_found = None
    results_start = None
    results_shown = None
    restaurants = None

    def __init__(self, **kwargs):
        self.results_found = kwargs.get("results_found", 0)
        self.results_start = kwargs.get("results_start", 0)
        self.results_shown = kwargs.get("results_shown", 0)
        self.restaurants = kwargs.get("restaurants", [])