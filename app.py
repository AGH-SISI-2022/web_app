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

    size = int(request_data['size'])
    popularity = request_data['popularity']
    start_time = request_data['start_time']

    # simulate work:
    if (size < 1000):
        time.sleep(5)
    elif (size < 10000):
        time.sleep(10)
    else:
        time.sleep(15)

    data = json.dumps({'size': size, 'popularity': popularity, 'start_time': start_time, 'end_time': datetime.now()}, default=str)

    # requests.post(url=url, data=data) # todo: uncomment this when url will be real

    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)