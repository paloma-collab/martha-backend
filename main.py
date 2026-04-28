from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "ok", "message": "Martha backend funcionando"})

if __name__ == '__main__':
    app.run()
