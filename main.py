from website.models import db, Product, Order



from main import db, app

with app.app_context():
    db.create_all()
    from website.models import Product
    product = Product(name='Sample Product', price=29.99, description='A great product', image_url='https://via.placeholder.com/150')
    db.session.add(product)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
