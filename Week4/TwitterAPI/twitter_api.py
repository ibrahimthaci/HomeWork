import requests, json

github_user = "joelgrus"  #can change the name user like ibrahimthaci etc
endpoint = f"https://api.github.com/users/{github_user}/repos"
repos = json.loads(requests.get(endpoint).text)
for i in repos:
    print(i)
