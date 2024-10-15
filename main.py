# main.py
from flask import Flask, render_template, request, redirect, url_for, session
from website.models import db, Product, Order
from website.config import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, SQLALCHEMY_DATABASE_URI

import stripe

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = 'mysecretkey'
db.init_app(app)

stripe.api_key = STRIPE_SECRET_KEY

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    return render_template('product.html', product=product)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        quantity = int(request.form.get('quantity'))
        order = Order(product_id=product_id, quantity=quantity)
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('cart'))

    orders = Order.query.all()
    return render_template('cart.html', orders=orders)

@app.route('/checkout', methods=['POST'])
def checkout():
    # Create a Stripe checkout session
    try:
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
            success_url=url_for('home', _external=True),
            cancel_url=url_for('cart', _external=True),
        )
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return str(e)
    


from main import db, app

with app.app_context():
    db.create_all()
    from website.models import Product
    product = Product(name='Sample Product', price=29.99, description='A great product', image_url='https://via.placeholder.com/150')
    db.session.add(product)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
