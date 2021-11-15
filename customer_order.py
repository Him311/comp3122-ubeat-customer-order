import flask
import pymongo

flask_app = flask.Flask(__name__)
mongo_client = pymongo.MongoClient('mongodb://comp3122:23456@customer_order_db:27017', serverSelectionTimeoutMS=2000)

db = mongo_client["customer_orders"]
col = db["Order"]

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=True, port=15000)

