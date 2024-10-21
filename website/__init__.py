
from flask import Config, Flask, app
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from sqlalchemy import text
import os

load_dotenv()

db = SQLAlchemy()



# Stripe Config (replace with your keys)
STRIPE_PUBLIC_KEY = 'your_public_key'
STRIPE_SECRET_KEY = 'your_secret_key'

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    database_url = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['STRIPE_PUBLIC_KEY'] = 'your_public_key'
    app.config['STRIPE_SECRET_KEY'] = 'your_secret_key'
    app.config.from_object(Config)
    
    db = SQLAlchemy(app)  # Initialize SQLAlchemy with the Flask app
    

    from .routes import routes
    from .views import views  
    
    app.register_blueprint(routes, url_prefix='/')  # Register Blueprints
    app.register_blueprint(views, url_prefix='/')  # Register Blueprints
    
    import traceback

    with app.app_context():
        return app
