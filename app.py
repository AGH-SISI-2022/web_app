import re
from flask import Flask, request
import time, json, requests
from datetime import datetime

app = Flask(__name__)

url = "http://localhost:5000" # todo: change to real url 

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/work', methods=['POST'])
def work():
    request_data = request.get_json()
    print('request data:', request_data)

    video_time = int(request_data['video_time'])

    # simulate work:
    if (video_time < 1000):
        for i in range(1000):
            i*i
    elif (video_time < 10000):
        for i in range(10000):
            i*i
    else:
        for i in range(100000):
            i*i

    # requests.post(url=url, data=data) # todo: uncomment this when url will be real

    return request_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)