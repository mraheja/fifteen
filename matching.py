import networkx as nx
import matplotlib.pyplot as plt
import json
import numpy as np



traits = ["extroversion","sensing","thinking","judging"]

#Matching Cost Kernel
def calculate_match(user_a, user_b):
  #Number of Matched Interests
  # sim_interests = 0
  # interests = set()
  # for interest in user_a['interests']:
  #   interests.add(interest)
  # for interest in user_b['interests']:
  #   if interest in interests:
  #     sim_interests += 1

  #Personality Squared Sum
  cost = 0
  for trait in traits:
    a_val = user_a['personality'][trait]
    b_val = user_b['personality'][trait]
    cost += (a_val - b_val)**2

  return cost

#Matching Algorithm
def find_matches(G):
    v = set()
    matches = []

    for edge in sorted(G.edges.data("weight")):
        a = edge[0]
        b = edge[1]
        w = edge[2]
        
        if(a in v or b in v):
            continue
            
        v.add(a)
        v.add(b)
        
        matches.append((a,b))

    dictt = {}
    match = []
    
    for e in matches:
      dicttt = {}
      dicttt['person1'] = e[0]
      dicttt['person2'] = e[1]
      match.append(dicttt)

    dictt['matches'] = match

    json.dump(dictt,open('matches.json','w'))
    
    return matches

def read_data():
  with open('dataCurrent.json') as json_file:
      G=nx.Graph()
      data = json.load(json_file)
      for user in data['users']:
        G.add_node(user['general']['name'])

      for i in range(len(data['users'])):
        for j in range(len(data['users'])):
          if i == j:
            continue
          relation = calculate_match(data['users'][i],data['users'][j])
          G.add_edge(data['users'][i]['general']['name'],data['users'][j]['general']['name'],weight=relation)
      return G


