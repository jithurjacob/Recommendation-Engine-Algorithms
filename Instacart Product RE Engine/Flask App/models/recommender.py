

def get_recommendations(cart_items):
    """Returns recommendations from all models"""
    DL_recommendations = ["a","b"]
    CF_recommendations = ["c","d"]
    return {"DeepLearning":DL_recommendations,"CollaborativeFiltering":CF_recommendations}

def get_products():
    return ["a","b"]