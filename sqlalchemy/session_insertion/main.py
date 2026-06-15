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

# Add a new product
new_product = Product(name="Laptop", description="High-end gaming laptop", price=1500)
session.add(new_product)
session.commit()

print(f"Added product: {new_product.name}")