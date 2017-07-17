from flask import Flask, render_template,jsonify, request
from models import recommender
app = Flask(__name__)

@app.route('/getRecommendations',methods=['POST'])
def getRecommendations():
    """Receieves the items in cart and returns the recommendations from all models"""
    return jsonify(recommendations=recommender.get_recommendations(request.form['cart_items']))

@app.route('/getProductDetails',methods=['GET'])
def getProductDetails():
    return jsonify(products=recommender.get_products())

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
