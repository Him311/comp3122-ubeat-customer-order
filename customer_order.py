import flask
import pymongo

flask_app = flask.Flask(__name__)
mongo_client = pymongo.MongoClient('mongodb://comp3122:23456@customer_order_db:27017', serverSelectionTimeoutMS=2000)

db = mongo_client["customer_orders"]
col = db["Order"]

@flask_app.route('/<order_id>', methods=['GET'])
def get_order(order_id):
    check = col.find_one({'order.order_id': order_id}, { '_id': 0})
    if check is None:
        return {'error': 'not found'}, 404
    else:
        order = col.find_one({'order.order_id': order_id}, { '_id': 0})['order']
        for x in order:
            if x['order_id'] == order_id:
                return x, 200

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=True, port=15000)

