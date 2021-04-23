import json

with open('./players.json') as p:
  data = json.load(p)
  
for key in data:
  if data.get(key).get("weight") == None:
    pass
  elif data.get(key).get("weight") > "350":
    print(data.get(key).get("full_name") + " is a chonker at " + data.get(key).get("weight") + " pounds!")
