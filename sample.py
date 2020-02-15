import json
from pprint import pprint

json_file=open('sample.json')
jdata = json.load(json_file)


"""
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

for user in jdata['users']: # for each user, get some data or something
  general = user['general']
  name = general['name']
  zip_code = general['zip code']
  gender = general['gender']
  year = general['year']

  personality = user['personality']
  extroversion = personality['extroversion']
  sensing = personality['sensing']

  # etc etc
  # now, somehow, update a bigass table to get put on a webpage
  

pprint (jdata)
json_file.close()