from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Initialize the database
engine = create_engine("sqlite:///data.db")
Base = declarative_base()

# Define the Product model
class Product(Base):
    __tablename__ = "products"
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
    {"name": "Headphones", "description": "Noise-cancelling headphones", "price": 200}
]

# Iterate through the list and add each product one by one
for product in products_to_add:
    new_product = Product(**product)  # Unpack the dictionary as keyword arguments
    session.add(new_product)
    session.commit()  # Commit after adding each product

# Update prices by reducing them by 20%
products_to_update = session.query(Product).all()

for product in products_to_update:
    old_price = product.price
    product.price = int(product.price * 0.8)  # Reduce price by 20%
    session.commit()  # Commit the change after updating the price
    print(f"Updated price for {product.name}: {old_price} -> {product.price}")