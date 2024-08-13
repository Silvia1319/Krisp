from flask import Flask, jsonify
import requests
import redis
from cachetools import TTLCache

app = Flask(__name__)
local_cache = TTLCache(maxsize=3, ttl=10)
redis_cache = redis.Redis(host='redis', port=6379, db=0)


def runcascade(viewer_id):
    models = ['model1', 'model2', 'model3', 'model4', 'model5']
    results = []
    for model_name in models:
        response = requests.post('http://generator:5000/generate',
                                 json={'model_name': model_name, 'viewerid': viewer_id})
        results.append(response.json())
    return results


@app.route('/recommend/<viewer_id>')
def recommend(viewer_id):
    if viewer_id in local_cache:
        return jsonify(local_cache[viewer_id])

    redis_result = redis_cache.get(viewer_id)
    if redis_result:
        return jsonify(eval(redis_result))

    result = runcascade(viewer_id)
    local_cache[viewer_id] = result
    redis_cache.setex(viewer_id, 30, str(result))
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000)
