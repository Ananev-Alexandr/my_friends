from app.users import user_api_ns
from flask_restx import Resource
from flask import request
from app.users.services import UserService


@user_api_ns.route('/registration', methods=['POST'])
class Registration(Resource):

    def post(self):
        params = request.get_json()
        return UserService.creat_user(params)

