from data_base.models import Post, db


class PostService():
    @classmethod
    def creat_post(cls, params: dict) -> dict:
        text_post = params.get('text_post')
        if PostService.validate_post(text_post) is False:
            return False
        post = Post()
        post.text_post = text_post
        #TODO user_id, MOCK
        post.user_id = 42
        db.session.add(post)
        db.session.commit()
        return {'message': 'Success add post!'}

    @classmethod 
    def validate_post(cls, text_post):
        if text_post is None:
            print("Пост не может быть пустым!")
            return False
        return True
        