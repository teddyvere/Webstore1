from flask import app
from website.models import db, Product, Order

app = create_app




with app.app_context():
    
    from website import db, create_app
    
    db.create_all()
    from website.models import Product
    product = Product(name='Sample Product', price=29.99, description='A great product', image_url='https://via.placeholder.com/150')
    db.session.add(product)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
