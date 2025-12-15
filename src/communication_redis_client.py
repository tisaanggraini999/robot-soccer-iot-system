import redis
import json

redis_db = redis.Redis(host="localhost", port=6379, decode_responses=True)

def publish_vision(data):
    redis_db.set("vision", json.dumps(data))

def get_vision():
    data = redis_db.get("vision")
    return json.loads(data) if data else None
