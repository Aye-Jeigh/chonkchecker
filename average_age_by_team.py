import json

with open('./players.json') as p:
  data = json.load(p)

agedata = {}

for key in data:
  age = data.get(key).get("age")
  team = data.get(key).get("team")
  if not age or team == "OAK":
    continue
  if not team:
    team = "unsigned"
  if team not in agedata:
      agedata[team] = []
  agedata[team].append(age)

for team, ages in agedata.items():
  print(F"The average age of {team} is {sum(ages) / len(ages):.3}")