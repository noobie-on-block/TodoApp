from flask import Flask
from config import config
from models import db


def create_app(config_name = 'testing'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
