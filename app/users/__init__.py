from flask import Blueprint
from flask_restx import Api
from flask_login import LoginManager


login = LoginManager()
user_bp = Blueprint('/', __name__)

user_api = Api(user_bp,
               doc=f'/swagger',
               catch_all_404s=True,
               title='User Service',
               description=f"Description for User Service API )",
               )

user_api_ns = user_api.namespace('/', description='All operation with User')
