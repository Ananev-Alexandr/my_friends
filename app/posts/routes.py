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
    
    
@user_api_ns.route('/all_posts', methods=['GET', 'POST'])
class AllPost(Resource):
    @login_required
    def get(self):
        return PostService.return_all_post()
    
    @login_required
    def post(self):
        params = request.get_json()
        return PostService.like_post(params)

@user_api_ns.route('/comment_post', methods=['POST', 'GET'])
class CommentPost(Resource):
    @login_required
    def post(self):
        params = request.get_json()
        return PostService.comment_post(params)
    
    @login_required
    def get(self):
        params = request.get_json()
        return PostService.all_comment_post(params)
    
    
@user_api_ns.route('/post_info/<post_id>', methods=['GET'])
class PostInfo(Resource):
    def get(self, post_id):
        return PostService.get_info_post(post_id)
    
    
    #TODO delete post
    #TODO delete comments?
    #TODO paginate
