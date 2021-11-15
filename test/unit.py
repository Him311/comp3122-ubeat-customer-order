import redis
import requests

redis_conn = redis.Redis(host='message_queue', port=6379)

def test_get_order():
    response = requests.get('http://customer_order:15000/r1o1')
    assert response.status_code == 200
    assert response.json() == {
        'order_id':'r1o1', 'restaurant_id':1, 'food_id':1, 'taken':1
    }

    