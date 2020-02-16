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

def get_current_match():
  json_file = open('dataCurrent.json')
  jdata = json.load(json_file)
  current_match = [user for user in jdata['users']]
  json_file.close()
  return current_match