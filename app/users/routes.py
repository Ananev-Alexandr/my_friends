from app.users import user_api_ns
from flask_restx import Resource
from flask import request
from app.users.services import UserService


@user_api_ns.route('/registration', methods=['POST'])
class Registration(Resource):

    def post(self):
        params = request.get_json()
        return UserService.creat_user(params)
    

@user_api_ns.route('/auth', methods=['POST'])
class Аuthorization(Resource):

    def post(self):
        auth_params = request.get_json()
        return UserService.auth(auth_params)
