import json

with open('./players.json') as p:
  data = json.load(p)

for key in data:
  weight = data.get(key).get("weight")
  fullname = data.get(key).get("full_name")
  if not weight:
    continue
  elif int(weight) > 350:
    print(F"{fullname} is a chonker at {weight} Pounds!")
