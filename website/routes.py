from flask import Blueprint, jsonify, redirect, render_template, request, flash, url_for
import stripe
from website.models import Order, Product
from . import db

# Create a Blueprint instance
routes = Blueprint('routes', __name__)

@routes.route('/product/<int:product_id>')
def product_view(product_id):
    return f"Product ID: {product_id}"

@routes.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity'))
        
        # Create a new order and add it to the database
        order = Order(product_id=product_id, quantity=quantity)
        db.session.add(order)
        db.session.commit()
        
        flash("Product added to cart successfully!", "success")
        return redirect(url_for('routes.cart'))

    orders = Order.query.all()
    return render_template('cart.html', orders=orders)

@routes.route('/checkout', methods=['POST'])
def checkout():
    try:
        # Create a Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Example Product',
                    },
                    'unit_amount': 1000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('routes.home', _external=True),
            cancel_url=url_for('routes.cart', _external=True),
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "danger")
        return redirect(url_for('routes.cart'))
