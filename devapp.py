from flask import Flask, request, jsonify, Response



app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
        return "Hello, World!", 200

@app.route("/health", methods=["GET"])
def health():
        return jsonify(status="ok"), 200

@app.route("/echo", methods=["POST"])
def echo():
        if request.is_json:
                return jsonify(received=request.get_json()), 200
        return Response(request.data or b"", mimetype="text/plain"), 200

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)# Zweryfikowano na Ubuntu
