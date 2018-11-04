import os
import json
import requests

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    url = "http://" + os.environ['BRANCH'] + ":8080"
    request = requests.get(url)
    chain = json.loads(request.text)
    print(type(chain))
    branch = dict()
    branch["microservice-beta"] = os.environ['BRANCH']
    chain.append(branch)
    return json.dumps(chain)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
