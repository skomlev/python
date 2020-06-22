# -*- coding: utf-8 -*-
from flask import Flask, jsonify

from api.states import states_api
from api.users import user_api
from extensions import db
from settings import DevelopmentConfig


def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_error_handlers(app)
    built_extensions(app)
    register_blueprints(app)
    return app


def built_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    app.register_blueprint(states_api, url_prefix="/api/states")
    app.register_blueprint(user_api, url_prefix="/api/users")


def register_error_handlers(app):

    @app.errorhandler(404)
    def render_error(error):
        return jsonify({"data": "Unkown service!", "success": False}), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({"data": "We're sorry :(", "success": False}), 500
