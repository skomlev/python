# coding: utf-8
from flask import Blueprint
from flask_restful import Api

from .resources import UsersResource


user_api = Blueprint('user_api', __name__)

api = Api(user_api)

api.add_resource(UsersResource, '/')

