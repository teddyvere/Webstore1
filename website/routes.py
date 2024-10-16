

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