from .restaurant.resource import RestaurantCollectionResource, RestaurantEntityResource
from .category.resource import CategoryCollectionResource
from flask import Blueprint
from flask_restful import Api
from flask import Flask
from config import POSTGRES_DBNAME, POSTGRES_USER, POSTGRES_HOST, POSTGRES_PASSWORD, APP_NAME
from db.postgress_connector import db

api_bp = Blueprint(APP_NAME, __name__)
api = Api(api_bp)

# Route
api.add_resource(RestaurantCollectionResource, '/restaurants')
api.add_resource(RestaurantEntityResource, '/restaurants/<id>')

api.add_resource(CategoryCollectionResource, '/categories')

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/' + APP_NAME)
app.config.from_object('config')

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PASSWORD, url=POSTGRES_HOST, db=POSTGRES_DBNAME)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)