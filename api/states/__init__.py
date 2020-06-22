# coding: utf-8
from flask import Blueprint
from flask_restful import Api

from .resources import StateResource


states_api = Blueprint('states_api', __name__)

api = Api(states_api)

api.add_resource(StateResource, '/')

