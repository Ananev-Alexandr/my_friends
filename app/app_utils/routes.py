from app.app_utils import utils_api_ns
from flask_restx import Resource


@utils_api_ns.route('/unauthorization', methods=['GET', 'POST'])
class Utils(Resource):
    
    def get(self):
        return {'message': "You are not authorizate!"}
    
    def post(self):
        return {'message': "You are not authorizate!"}
    