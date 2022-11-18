from data_base.models import Post, db
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
