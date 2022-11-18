from flask import Blueprint
from flask_restx import Api


post_bp = Blueprint('/post', __name__)
authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}
post_api = Api(post_bp,
               doc=f'/swagger',
               catch_all_404s=True,
               title='Post Service',
               description=f"Description for Post Service API )",
               authorizations=authorizations
               )

post_api_ns = post_api.namespace('/', description='All operation with Post')

from app.posts import routes
