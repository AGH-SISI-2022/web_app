from flask import Flask, request, jsonify
import requests, time

app = Flask(__name__)

url = "management.default.svc.cluster.local:8080"

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/send', methods=['POST'])
def send():
    requests.post(url=url + '/send', data=request.get_json())

    resp = jsonify(success=True)
    return resp

@app.route('/watch', methods=['POST'])
def watch():
    request_data = request.get_json()
    print('request data:', request_data)

    video_time = int(request_data['video_time'])

    simulate_time = 0

    # simulate work:
    if (video_time < 1000):
        simulate_time = 2

    elif (video_time < 100000):
        simulate_time = 5

    else:
        simulate_time = 10

    timeout = time.time() + float(simulate_time)

    while True:
        if time.time() > timeout:
            break

    resp = jsonify(success=True)
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)