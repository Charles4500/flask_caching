import datetime
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_caching import Cache
import redis

from models.items import db, Item

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cache.db'
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_HOST'] = 'localhost'
app.config['CACHE_REDIS_PORT'] = 6379
app.config['CACHE_REDIS_DB'] = 0


db.init_app(app)
cache = Cache()
cache.init_app(app)
migrate = Migrate(app=app,db=db)
# Initializing Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)


app.route('/items', methods=['POST'])


def add_item():
    # Getting the item name from the request bdy
    item_name = request.json.get('name')

    # Delete the cached response to invalidate the cache
    cache.delete('items')
    return jsonify({'message': 'Item added successfuly'})


@app.route('/items', methods=['GET'])
@cache.cached(timeout=60, key_prefix='items')
def get_items():
    # Check if the response is already cached
    cached_response = redis.client.get('items')
    if cached_response:
        return jsonify(cached_response)

    # Getting all items from the database
    items = Item.query.all()

    all_items = [item.to_dict() for item in items]

    return all_items


if __name__ == '__main__':
    app.run(port=5080, debug=True, host='0.0.0.0')
