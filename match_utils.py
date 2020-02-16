import json
from pprint import pprint

""" 
get_past_matches() returns a dictionary of a user's matches, which are
individual dictionaries.
Sample user data:
    {
      "general" : {
        "name" : "John Smith",
        "zip code" : 94555,
        "gender" : "male",
        "year" : 1
      },
      "personality" : {
        "extroversion" : 0.91,
        "sensing" : 0.32,
        "thinking" : 0.75,
        "judging" : 0.04
      },
      "interests" : [1, 5, 8]
    }
"""

def get_past_matches():
  json_file = open('dataPast.json')
  jdata = json.load(json_file)
  past_matches = [user for user in jdata['users']]
  json_file.close()
  return past_matches

def get_current_match(user): #user is a string
  json_matches = open('matches.json')
  match_data = json.load(json_matches)
  json_current = open('dataCurrent.json')
  current_data = json.load(json_current)

  usr = None
  for dict in match_data['matches']:
    if user == dict["person1"]:
      usr = dict["person2"]
    elif user == dict["person2"]:
      usr = dict["person1"]
  
  for user in json_current['users'][0]:
    if user.general.name.equals(user):
      json_matches.close()
      json_current.close()
      return user

  json_matches.close()
  json_current.close()
  return None