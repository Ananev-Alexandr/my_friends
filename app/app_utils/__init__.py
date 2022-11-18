from flask import Blueprint
from flask_restx import Api


utils_bp = Blueprint('/utils', __name__)
authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Utils'
    }
}
utils_api = Api(utils_bp,
               doc=f'/swagger',
               catch_all_404s=True,
               title='Utils Service',
               description=f"Description for Utils Service API )",
               authorizations=authorizations
               )

utils_api_ns = utils_api.namespace('/', description='All operation with Utils')

from app.app_utils import routes
