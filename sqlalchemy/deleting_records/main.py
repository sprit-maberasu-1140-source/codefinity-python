from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Initialize the database
engine = create_engine("sqlite:///example.db")
Base = declarative_base()

# Define the Product model
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    is_in_stock = Column(Boolean, default=True)

# Create tables
Base.metadata.create_all(engine)

# Set up the session
Session = sessionmaker(bind=engine)
session = Session()

# Add multiple products (one at a time)
products_to_add = [
    {"name": "Laptop", "description": "High-end gaming laptop", "price": 1500},
    {"name": "Smartphone", "description": "Latest model smartphone", "price": 800},
    {"name": "Headphones", "description": "Noise-cancelling headphones", "price": 200, "is_in_stock": False}
]

# Iterate through the list and add each product one by one
for product in products_to_add:
    new_product = Product(**product)  # Unpack the dictionary as keyword arguments
    session.add(new_product)
    session.commit()  # Commit after adding each product

# Delete the product 'Headphones'
headphones_to_delete = session.query(Product).filter(Product.name == "Headphones").first()

if headphones_to_delete:
    session.delete(headphones_to_delete)  # Delete the product
    session.commit()  # Commit the deletion
    print(f"Deleted product: {headphones_to_delete.name}")

# Retrieve and display all products after deletion
retrieved_products = session.query(Product).all()
print("\nAll products in the database after deletion:")
for product in retrieved_products:
    print(product.name)