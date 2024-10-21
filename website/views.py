from flask import Blueprint, render_template
from .models import Product

# Create the Blueprint
views = Blueprint('views', __name__)

# Define your route using the Blueprint
@views.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)
