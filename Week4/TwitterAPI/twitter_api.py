import requests, json

github_user = "ibrahimthaci"
endpoint = f"https://api.github.com/users/{github_user}/repos"
repos = json.loads(requests.get(endpoint).text) #loads request in text form, json type
for i in repos:
    print(i)
