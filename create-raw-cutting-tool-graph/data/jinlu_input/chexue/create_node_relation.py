from py2neo import *
import pandas as pd
import numpy as np
import tqdm

graph = Graph('http://localhost:7474',password = '123456')
file = pd.read_excel('data/root_node_relation.xlsx')
data = np.array(file)
data = data.tolist()
sum = 0
for line in tqdm.tqdm(data):
    node_head = graph.nodes.match('{node_class}'.format(node_class = line[3])).where(name='{name}'.format(name=line[0])).first()
    node_tail = graph.nodes.match('{node_class}'.format(node_class = line[3])).where(name='{name}'.format(name=line[2])).first()
    matcher = RelationshipMatcher(graph)
    relation = matcher.match((node_head,node_tail),r_type='{rel}'.format(rel=line[1])).first()
    if relation!= None:
        continue
    sum = sum+1
    r = Relationship(node_head,'{rel}'.format(rel=line[1]),node_tail)
    graph.create(r)
print('created %d relations'%sum)

