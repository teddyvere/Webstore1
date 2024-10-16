from flask import Flask, render_template
from models import db, Product

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)