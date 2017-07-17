from .CollaborativeFiltering import CF_recommender
from .DeepLearning import DL_recommender
def get_recommendations(cart_items):
    """Returns recommendations from all models"""
    DL_recommendations = DL_recommender.get_recommendations(cart_items)
    CF_recommendations = CF_recommender.get_recommendations(cart_items)
    return {"DeepLearning":DL_recommendations,"CollaborativeFiltering":CF_recommendations}

def get_products():
    return open("./models/product_list.txt").read().splitlines()