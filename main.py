from website import create_app, db  # Ensure you're importing the right items
from website.models import Product

app = create_app()

with app.app_context():  # Ensure you are in the app context
    db.create_all()  # This will create all tables in the database
    product = Product(name='Sample Product', price=29.99, description='A great product', image_url='https://via.placeholder.com/150')
    db.session.add(product)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
