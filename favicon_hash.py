from flask import Flask, request
import mmh3
import requests
import codecs

app = Flask(__name__)

@app.route('/favicon', methods=['GET'])
def favicon_hash():
    url = request.args.get('url')
    try:
        url = url + '/favicon.ico'
        response = requests.get(url)
        if response.status_code == 200:
            favicon = codecs.encode(response.content, 'base64')
            hash = mmh3.hash(favicon)
            return "{http.favicon.hash:%d}" % hash
    except requests.exceptions.ConnectionError as e:
        return "{http.favicon.hash:favicon.ico not availabe}"
    return "{http.favicon.hash:favicon.ico not available}"

if __name__ == '__main__':
    app.run(debug=True)

#http://localhost:5000/favicon?url=https://www.google.com