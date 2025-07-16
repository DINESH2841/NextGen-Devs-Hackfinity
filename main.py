from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db import engine, Base, SessionLocal
import models
from routers import (
    auth_routes, product_routes, category_routes, catalog_routes,
    feedback_routes, contact_routes, suggestion_routes,
    top_sold_routes, translate_routes
)


# Create all database tables
# This should be handled with Alembic in a real production app
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI-Powered Digital Catalog Assistant")

# Add CORS middleware to allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include all the routers
app.include_router(auth_routes.router)
app.include_router(product_routes.router)
app.include_router(category_routes.router)
app.include_router(catalog_routes.router)
app.include_router(feedback_routes.router)
app.include_router(contact_routes.router)
app.include_router(suggestion_routes.router)
app.include_router(top_sold_routes.router)
app.include_router(translate_routes.router)


@app.on_event("startup")
def startup_event():
    """
    Event handler for application startup.
    This function populates the database with some dummy data if it's empty.
    """
    db = SessionLocal()
    # Check if categories exist
    if db.query(models.Category).count() == 0:
        print("Database is empty. Populating with dummy data...")
        populate_db(db)
    else:
        print("Database already contains data. Skipping population.")
    db.close()

def populate_db(db: Session):
    """
    Populates the database with initial dummy categories and products.
    """
    # Create dummy categories
    categories = [
        models.Category(name="Spices", name_hi="मसाले", name_ta="மசாலா", name_te="మసాలాలు", name_bn="মশলা"),
        models.Category(name="Vegetables", name_hi="सब्जियां", name_ta="காய்கறிகள்", name_te="కూరగాయలు", name_bn="সবজি"),
        models.Category(name="Grains", name_hi="अनाज", name_ta="தானியங்கள்", name_te="ధాన్యాలు", name_bn="শস্য"),
        models.Category(name="Handicrafts", name_hi="हस्तशिल्प", name_ta="கைவினைப்பொருட்கள்", name_te="హస్తకళలు", name_bn="হস্তশিল্প")
    ]
    db.add_all(categories)
    db.commit()

    # Create dummy products
    products = [
        models.Product(name="Turmeric Powder", description="Freshly ground turmeric powder with high curcumin content.", price=50.0, quantity_unit="200g", category_id=1, sales_count=150, image_url="https://i.imgur.com/example-turmeric.jpg"),
        models.Product(name="Fresh Tomatoes", description="Juicy, ripe tomatoes sourced from local farms.", price=40.0, quantity_unit="1kg", category_id=2, sales_count=220, image_url="https://i.imgur.com/example-tomatoes.jpg"),
        models.Product(name="Basmati Rice", description="Premium quality long-grain Basmati rice.", price=120.0, quantity_unit="1kg", category_id=3, sales_count=180, image_url="https://i.imgur.com/example-rice.jpg"),
        models.Product(name="Handmade Clay Pot", description="Eco-friendly clay pot, perfect for cooking and serving.", price=250.0, quantity_unit="1 piece", category_id=4, sales_count=90, image_url="https://i.imgur.com/example-pot.jpg"),
        models.Product(name="Red Chilli Powder", description="Spicy and flavorful red chilli powder.", price=60.0, quantity_unit="200g", category_id=1, sales_count=300, image_url="https://i.imgur.com/example-chilli.jpg")
    ]
    db.add_all(products)
    db.commit()
    print("Dummy data has been added to the database.")


@app.get("/api")
def read_root():
    return {"message": "Welcome to the AI Digital Catalog Assistant API"}