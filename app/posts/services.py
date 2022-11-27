from data_base.models import Post, Comment, LikePost, db
from flask_login import current_user

class PostService():
    @classmethod
    def creat_post(cls, params: dict) -> dict:
        text_post = params.get('text_post')
        if PostService.validate_post(text_post) is False:
            return False
        post = Post()
        post.text_post = text_post
        post.user_id = current_user.get_id()
        db.session.add(post)
        db.session.commit()
        return {'message': 'Success add post!'}

    @classmethod 
    def validate_post(cls, text_post):
        if text_post is None:
            print("Пост не может быть пустым!")
            return False
        return True
    
    @classmethod
    def return_all_post(cls):
        result = {"data": []}
        posts :list[Post]= Post.query.order_by(Post.publication_date).all()
        for element in posts:
            result["data"].append(element.to_json())
        return result

    @classmethod
    def comment_post(cls, params):
        text_comment = params.get('text_comment')
        post_id = params.get('post_id')
        comment = Comment()
        comment.text_comment = text_comment
        comment.post_id = post_id
        comment.user_id = current_user.get_id()
        db.session.add(comment)
        db.session.commit()
        return {'message': 'Success add comment to post!'}
    
    @classmethod
    def all_comment_post(cls, params):
        post_id = params.get('post_id')
        result = {"data": []}
        com = Comment.query.filter(Comment.post_id == str(post_id)).all()
        for element in com:
            result["data"].append(element.to_json())
        return result
    
    @classmethod
    def like_post(cls, params):
        def result_all_likes():
            return LikePost.query.filter(LikePost.post_id == post_id).count()
        post_id = params.get('post_id')
        likepost = LikePost.query.filter(
            LikePost.post_id==post_id,
            LikePost.user_id==current_user.get_id()
            ).one_or_none()
        if likepost is None:
            lp = LikePost()
            lp.post_id = post_id
            lp.user_id = current_user.get_id()
            db.session.add(lp)
            db.session.commit()
            return {'message': f"you like it, and now {result_all_likes()} likes!"}
        else:
            db.session.delete(likepost)
            db.session.commit()
            return {'message': f"you delete like, and now {result_all_likes()} likes!"}
        