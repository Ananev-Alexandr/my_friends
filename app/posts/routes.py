from app.users import user_api_ns
from flask_restx import Resource
from flask import request
from app.posts.services import PostService
from flask_login import login_required


@user_api_ns.route('/posts', methods=['POST'])
class Post(Resource):
    @login_required
    def post(self):
        params = request.get_json()
        return PostService.creat_post(params)
