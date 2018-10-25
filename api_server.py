from flask import Flask
app = Flask(__name__)


@app.route('/readHello')
def getRequestHello():
    return "Hi, I got your GET Request!"


@app.route('/createHello', methods=['POST'])
def postRequestHello():
    return "I see you sent a POST message :-)"


@app.route('/updateHello', methods=['PUT'])
def updateRequestHello():
    return "Sending Hello on an PUT request!"


@app.route('/deleteHello', methods=['DELETE'])
def deleteRequestHello():
    return "Deleting your hard drive.....haha just kidding!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
