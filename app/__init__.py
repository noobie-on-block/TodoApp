from flask import Flask
from config import config
from app.models import db
from app.api_blueprints import api as api_blueprint
from app.main_blueprints import view as view_blueprint


def create_app(config_name = 'testing'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(view_blueprint)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
