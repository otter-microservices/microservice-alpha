import os
import json
import requests

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    url = "http://" + os.environ['UPSTREAM_SERVICE'] + "." + os.environ['BRANCH'] + "-" + os.environ['UPSTREAM_SERVICE'] + os.environ['UPSTREAM_PORT']
    request = requests.get(url, timeout=0.5)
    chain = json.loads(request.text)
    print(type(chain))
    branch = dict()
    branch["microservice-beta"] = os.environ['BRANCH']
    chain.append(branch)
    return json.dumps(chain)

@app.route('/healthz')
def healthz():
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
