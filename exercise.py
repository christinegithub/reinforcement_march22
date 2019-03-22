import requests
import json

# res = requests.get("https://cdn.rawgit.com/everypolitician/everypolitician-data")
# res = requests.get("http://everypolitician.org/uzbekistan/")

res = requests.get("https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json")
body = json.loads(res.content)

# Search index for country

# i = 0
# for i, country in enumerate(body):
#         print(country["name"])
#         print(i)

belarus_url = body[20]["legislatures"][0]["popolo_url"]

print(belarus_url)

res_belarus = requests.get(belarus_url)
body_belarus = json.loads(res_belarus.content)

politician_1 = body_belarus["persons"][0]["name"]

print(politician_1)
