from app.users import user_api_ns
from flask_restx import Resource
from flask import request
from app.users.services import UserService
from flask_login import login_required


@user_api_ns.route('/registration', methods=['POST', 'GET'])
class Registration(Resource):
    #TODO add check unauthorization
    def post(self):
        params = request.get_json()
        return UserService.creat_user(params)


@user_api_ns.route('/login', methods=['POST'])
class Login(Resource):
    #TODO add check unauthorization
    def post(self):
        login_params = request.get_json()
        return UserService.login(login_params)


@user_api_ns.route('/logout', methods=['POST'])
class Logout(Resource):
    @login_required
    def post(self):
        return UserService.logout()


@user_api_ns.route('/all_users', methods=['GET'])
class AllUsers(Resource):
    @login_required
    def get(self):
        return UserService.return_all_users()
    
@user_api_ns.route('/filter_users', methods=['GET'])
class FilterUsers(Resource):
  
    @login_required
    def get(self):
        params = request.get_json()
        return UserService.filter_users(params)
