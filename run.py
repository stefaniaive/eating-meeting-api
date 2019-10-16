from flask import Flask
from config import APP_NAME

app = Flask(__name__)

from app import api_bp
app.register_blueprint(api_bp, url_prefix='/' + APP_NAME)

if __name__ == '__main__':
    app.run()