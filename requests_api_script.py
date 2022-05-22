import requests

ENDPOINT_APP_ID = 'endpoint url'
TOKEN_API_KEY = 'api key'

headers = {
    'header key': 'header value',
}

ENDPOINT_APP_ID = {
    'param key': 'param value',
}

response = requests.get(url=ENDPOINT_APP_ID, params=ENDPOINT_APP_ID, headers=headers)
status = response.raise_for_status()
data = response.json()
