import json

with open("keymap.json") as jsonData:
    keymap=json.load(jsonData)

 
#serach "1_4" out ->"k"
print(keymap["14"])