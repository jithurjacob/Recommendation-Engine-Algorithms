import pandas as pd
import json

def get_recommendations(cart_items):
    cart_items =  json.loads(cart_items)
    last_item = cart_items[-1]
    df = pd.read_excel("./models/CollaborativeFiltering/CollaborativeFiltered.xlsx") 
    print(cart_items)
    print(last_item)
    print(df.loc[df["product_id"]==last_item].values.tolist())
    vals = (df.loc[df["product_id"]==last_item].values.tolist())
    if len(vals) != 0:
        return vals[0][2:6]
    return  vals