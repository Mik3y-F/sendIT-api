from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy


# Local import 
from instance.config import app_config


# initialized sqlalchemy
db = SQLAlchemy()


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .api.v1.routes.routes import api

    app.register_blueprint(api, url_prefix='/api/v1')

    return app
