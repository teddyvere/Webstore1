# config.py
import os

SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
SQLALCHEMY_DATABASE_URI = 'sqlite:///store.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Stripe Config (replace with your keys)
STRIPE_PUBLIC_KEY = 'your_public_key'
STRIPE_SECRET_KEY = 'your_secret_key'
