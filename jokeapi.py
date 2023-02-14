from flask import Flask, jsonify
import pyjokes

app = Flask(__name__)

@app.route('/joke', methods=['GET'])
def joke():
    return jsonify(joke=pyjokes.get_joke())

if __name__ == '__main__':
    app.run()
# http://localhost:5000/joke