import networkx as nx
import matplotlib.pyplot as plt
import json

G=nx.Graph()

def calculate_match(user_a, user_b):
  #Number of Matched Interests
  interests = set()
  for interest in user_a['interests']:
    
  #Personality Squared Sum


  return user_a['']

with open('data.txt') as json_file:

    data = json.load(json_file)
    for user in data['users']:
      G.add_node(user['general']['name'])

    for i in range(len(data['users'])):
      for j in range(len(data['users'])):
        if i == j:
          continue
        G.add_edge(i,j)
        G.add_node(user['general']['name'])

print(G)
