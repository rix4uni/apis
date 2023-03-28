import mmh3
import requests
import codecs
import sys
import random

urls = sys.stdin.read().splitlines()

# Send a request
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
]
headers = {"User-Agent": random.choice(user_agents)}

for url in urls:
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            favicon = codecs.encode(response.content, 'base64')
            hash = mmh3.hash(favicon)
            print(f"{url}: http.favicon.hash:{hash}")
    except requests.exceptions.ConnectionError as e:
        pass

# cat urls.txt | python3 favicon_hash_cli.py
# echo "https://dell.com/favicon.ico" | python3 favicon_hash_cli.py