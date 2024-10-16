
from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from sqlalchemy import text
import os

load_dotenv()

db = SQLAlchemy()

SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'sqlite:///store.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Stripe Config (replace with your keys)
STRIPE_PUBLIC_KEY = 'your_public_key'
STRIPE_SECRET_KEY = 'your_secret_key'
