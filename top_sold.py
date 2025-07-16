from sqlalchemy.orm import Session
from . import models

def get_top_selling_products(db: Session, limit: int = 5):
    """
    Gets the top-selling products based on the 'sales_count' field.
    """
    top_products = (
        db.query(models.Product)
        .order_by(models.Product.sales_count.desc())
        .limit(limit)
        .all()
    )
    print(f"📈 Top Sold: Returning {len(top_products)} top-selling products.")
    return top_products