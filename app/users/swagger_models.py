from app.users import user_api_ns
from flask_restx import fields


login_data = user_api_ns.model("login_data", {
    'login': fields.String(required=True, example='12test'),
    'user_password': fields.String(required=True, example='12121212')
})

response_success = user_api_ns.model("response_success", {
    'message': fields.String(example='Success')
})

login_failed = user_api_ns.model("login_failed", {
    'message': fields.String(example='Wrong login or password')
})