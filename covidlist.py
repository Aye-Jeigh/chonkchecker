import json

with open('./players.json') as p:
  data = json.load(p)

injurylist = ["Sus", "Questionable","Out","IR","NA"]

for key in data:
  fullname = data.get(key).get("full_name")
  injury = data.get(key).get("injury_status")
  if not injury:
    continue
  if injury in injurylist:
    continue
  else:
    print(F"{fullname} has got the covid")