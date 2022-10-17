import requests
import json
import webbrowser

r = requests.get("")

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
