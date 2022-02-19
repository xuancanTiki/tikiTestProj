from flask import Flask
from flask import jsonify
from flask import request
import socket
app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_geek():

    return jsonify({'Client IP` ': request.remote_addr,
                    'Host:': socket.gethostname(),
                    'User-Agent:': request.headers.get('User-Agent'),
                    'Accept': request.headers.get('accept')
                    }), 200

if __name__ == "__main__":
    app.run(port=8080,host='0.0.0.0',debug=True)
