from flask import Flask, jsonify
import pyjokes

app = Flask(__name__)

@app.route('/joke', methods=['GET'])
def joke():
    return jsonify(joke=pyjokes.get_joke())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

# http://localhost:81/joke
# https://joke.rix4uni.repl.co/joke