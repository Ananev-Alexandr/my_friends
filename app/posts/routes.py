from app.users import user_api_ns
from flask_restx import Resource
from flask import request
from app.posts.services import PostService
from flask_login import login_required


@user_api_ns.route('/posts', methods=['POST'])
class Post(Resource):
    @login_required
    def post(self):
        "Create post"
        params = request.get_json()
        return PostService.creat_post(params)
    
    
@user_api_ns.route('/all_posts', methods=['GET'])
class AllPost(Resource):
    @login_required
    def get(self):
        """View all posts"""
        return PostService.return_all_post()

@user_api_ns.route('/like', methods=['POST'])
class AllPost(Resource):
    @login_required
    def post(self):
        """Create or delete 'like' on the post"""
        params = request.get_json()
        return PostService.like_post(params)

@user_api_ns.route('/comment_post', methods=['POST', 'GET'])
class CommentPost(Resource):
    @login_required
    def post(self):
        """Сreate a comment for a post"""
        params = request.get_json()
        return PostService.comment_post(params)
    
    @login_required
    def get(self):
        """Getting all comments on a post"""
        params = request.get_json()
        return PostService.all_comment_post(params)
    
    
@user_api_ns.route('/post_info/<post_id>', methods=['GET'])
class PostInfo(Resource):
    def get(self, post_id):
        """Get full information about post by id (post content, like count, comments)"""
        return PostService.get_info_post(post_id)
    
    
    #TODO delete post
    #TODO delete comments?
    #TODO paginate
