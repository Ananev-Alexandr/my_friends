from app.users import user_api_ns
from flask_restx import Resource
from flask import request, jsonify
from app.users.services import UserService


# @bp_user.route('/test')
# # def test_route():
    
@user_api_ns.route('/test', methods=['POST'])
class Test(Resource):
    
    def post(self):
        param = request.get_json()
        print(param)
        return jsonify({"message": "success"})
    
@user_api_ns.route('/registration', methods=['POST'])
class Registration(Resource):
    
    def post(self):
        params = request.get_json()
        return UserService.creat_user(params)
        
        