from flask import Flask, request
import requests

app = Flask(__name__)

url = "management.default.svc.cluster.local:8080" # todo: add path to url

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/watch', methods=['POST'])
def watch():
    request_data = request.get_json()
    print('request data:', request_data)

    requests.post(url=url, data=request_data)

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

    return request_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)