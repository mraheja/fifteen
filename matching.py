import networkx as nx
import matplotlib.pyplot as plt
import json
import numpy as np

G=nx.Graph()

traits = ["extroversion","sensing","thinking","judging"]

#Matching Cost Kernel
def calculate_match(user_a, user_b):
  #Number of Matched Interests
  sim_interests = 0
  interests = set()
  for interest in user_a['interests']:
    interests.add(interest)
  for interest in user_b['interests']:
    if interest in interests:
      sim_interests += 1

  #Personality Squared Sum
  cost = 0
  for trait in traits:
    a_val = user_a['personality'][trait]
    b_val = user_b['personality'][trait]
    cost += (a_val - b_val)**2

  return cost

#Matching Algorithm
def find_matches(G):
    pass

with open('data.json') as json_file:

    data = json.load(json_file)
    for user in data['users']:
      G.add_node(user['general']['name'])

    for i in range(len(data['users'])):
      for j in range(len(data['users'])):
        if i == j:
          continue
        relation = calculate_match(data['users'][i],data['users'][j])
        G.add_edge(data['users'][i]['general']['name'],data['users'][j]['general']['name'],weight=relation)

nx.draw_networkx(G,with_labels=True)
