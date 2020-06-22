# coding: utf-8
from flask import jsonify
from flask_restful import Resource


class StateResource(Resource):

    def get(self):

        return jsonify({"data": 'States is alive', "success": True})

    def post(self):
        pass

