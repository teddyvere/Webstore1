from flask import Blueprint, Flask, app, render_template
from models import db, Product

views = Blueprint('views', __name__)

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)