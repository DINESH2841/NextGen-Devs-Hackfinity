def get_product_suggestions(product_id: int, db):
    """
    Mocks a recommendation engine.
    In a real app, this would use collaborative filtering, content-based filtering,
    or an AI model to find related products.
    For this demo, it just returns a few random products from the same category.
    """
    from . import models

    # Find the current product's category
    current_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not current_product:
        return []

    # Find other products in the same category, excluding the current one
    suggestions = (
        db.query(models.Product)
        .filter(models.Product.category_id == current_product.category_id)
        .filter(models.Product.id != product_id)
        .limit(3)
        .all()
    )
    
    print(f"💡 Mock Suggestions: Recommending {len(suggestions)} products from the same category for product ID {product_id}.")
    
    return suggestions