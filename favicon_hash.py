from flask import Flask, request
import mmh3
import requests
import codecs

app = Flask(__name__)

@app.route('/favicon', methods=['GET'])
def favicon_hash():
    url = request.args.get('url')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            favicon = codecs.encode(response.content, 'base64')
            hash = mmh3.hash(favicon)
            return "http.favicon.hash:" + str(hash)
    except requests.exceptions.ConnectionError as e:
        return "http.favicon.hash:favicon.ico not available"
    return "http.favicon.hash:favicon.ico not available"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

# http://localhost:81/favicon?url=https://www.google.com/favicon.ico
# https://favicon.rix4uni.repl.co/favicon?url=https://www.udemy.com/staticx/udemy/images/v8/favicon-32x32.png