import sqlite3
from .CollaborativeFiltering import CF_recommender
from .DeepLearning import DL_recommender
def get_recommendations(cart_items):
    """Returns recommendations from all models"""
    DL_recommendations = DL_recommender.get_recommendations(cart_items)
    CF_recommendations = CF_recommender.get_recommendations(cart_items)
    return {"DeepLearning":DL_recommendations,"CollaborativeFiltering":CF_recommendations}

def get_products():
    return open("./models/product_list.txt").read().splitlines()

def get_users():
    with sqlite3.connect("./db/db.sqlite") as conn:
        sql = "select * from user"
        users = conn.execute(sql).fetchall()
    return users

def get_coupons(user_id,user_emotion):
    """Returns the coupons
    
    High-spender, Happy or Neutral - no coupon
    High-spender, Sad - 10% coupon
    High-spender, Angry - 20% coupon
    Average-spender, Happy or Neutral - no coupon
    Average-spender, Sad - no coupon
    Average-spender, Angry - 10% coupon
    Low-spender, Happy or Neutral - no coupon
    Low-spender, Sad - no coupon
    Low-spender, Angry - 5% coupon
    Frequent-returner, Happy or Neutral - no coupon
    Frequent-returner, Sad - no coupon
    Frequent-returner, Angry - no coupon
    """
    
    with sqlite3.connect("./db/db.sqlite") as conn:
        sql = "select user_type from user where id=%s"%user_id
        #print(sql)
        user_type = conn.execute(sql).fetchone()
    coupon = "No Coupon"
    print(user_type,user_emotion)
    if user_type:
        user_type = user_type[0]
        if user_type == "High-spender" and user_emotion == "Sad":
            coupon = "10% Coupon"
        elif user_type == "High-spender" and user_emotion == "Angry":
            coupon = "20% Coupon"
        elif user_type == "Average-spender" and user_emotion == "Angry":
            coupon = "10% Coupon"   
        elif user_type == "Low-spender" and user_emotion == "Angry":
            coupon = "5% Coupon"  
    else:
        return "Invalid User Id"
    return coupon
    
