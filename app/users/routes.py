from app.users import user_api_ns
from flask_restx import Resource
from flask import request
from app.users.services import UserService
from flask_login import login_required, current_user
from app.users import swagger_models


@user_api_ns.route('/registration', methods=['POST', 'GET'])
class Registration(Resource):
    def post(self):
        """Create user"""
        if current_user.is_authenticated:
            return {'message': 'you have to log out'}
        params = request.get_json()
        return UserService.creat_user(params)


@user_api_ns.route('/login', methods=['POST'])
class Login(Resource):
    @user_api_ns.expect(swagger_models.login_data)
    @user_api_ns.response(200, swagger_models.response_success)
    @user_api_ns.response(400, swagger_models.login_failed)
    def post(self):
        """Sign in"""
        if current_user.is_authenticated:
            return {'message': 'you have to log out'}
        login_params = request.get_json()
        return UserService.login(login_params)


@user_api_ns.route('/logout', methods=['POST'])
class Logout(Resource):
    @login_required
    def post(self):
        """Sign out"""
        return UserService.logout()


@user_api_ns.route('/all_users', methods=['GET'])
class AllUsers(Resource):
    @login_required
    def get(self):
        """Getting all users"""
        return UserService.return_all_users()
    
@user_api_ns.route('/filter_users', methods=['GET'])
class FilterUsers(Resource):
    @login_required
    def get(self):
        """Filtering users by passed parameters"""
        params = request.get_json()
        return UserService.filter_users(params)
