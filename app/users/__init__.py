from flask import Blueprint
from flask_restx import Api


user_bp = Blueprint('/', __name__)
authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}
user_api = Api(user_bp,
               doc=f'/swagger',
               catch_all_404s=True,
               title='User Service',
               description=f"Description for User Service API )",
               authorizations=authorizations
               )

user_api_ns = user_api.namespace('/', description='All operation with User')

from app.users import routes