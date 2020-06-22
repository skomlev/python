# coding: utf-8
from flask import jsonify
from flask_restful import Resource



class UsersResource(Resource):

    def get(self, user_id=None):

        return jsonify({"data": 'Users alive', "success": True})

    def post(self):
        pass

    def delete(self, user_id=None):
        pass
