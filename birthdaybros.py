import json

with open('./players.json') as p:
  data = json.load(p)

birthdayinput = input("Enter your birthday in year-month-date format: ")

for key in data:
  bday = data.get(key).get("birth_date")
  fullname = data.get(key).get("full_name")
  if not bday:
    continue
  elif bday == birthdayinput:
    print(F"{fullname} is your birthday bro")
