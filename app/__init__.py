from flask import Flask
from flask_migrate import Migrate
from config import Config
from data_base.models import db
from dotenv import load_dotenv
from app.users import user_bp
from app.posts import post_bp


migrate = Migrate()
load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app, db)
app.register_blueprint(user_bp)
app.register_blueprint(post_bp)
db.app = app
