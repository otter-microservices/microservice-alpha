import os
import json
import requests

from flask import Flask
app = Flask(__name__)

microservice-alpha.master-microservice-alpha

@app.route('/')
def hello_world():
    url = "http://" + "os.environ['UPSTREAM_SERVICE']"+ os.environ['BRANCH'] + "-" + os.environ['UPSTREAM_SERVICE'] + ":8080"
    request = requests.get(url)
    chain = json.loads(request.text)
    print(type(chain))
    branch = dict()
    branch["microservice-beta"] = os.environ['BRANCH']
    chain.append(branch)
    return json.dumps(chain)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
