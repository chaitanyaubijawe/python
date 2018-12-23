


import json

file = open("fact.json")
# string....
data = file.read()


jsonObj = json.loads(data)

print(jsonObj)

# sh deployment.sh -r ap-northeast-1 -e qa -v chaitanya
