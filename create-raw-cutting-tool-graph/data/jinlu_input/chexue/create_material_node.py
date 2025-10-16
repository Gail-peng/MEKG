from py2neo import *
import pandas as pd
import numpy as np
import tqdm


graph = Graph('http://localhost:7474',password = '123456')
file = pd.read_excel('data/material.xlsx')
data = np.array(file)
data = data.tolist()

sum = 0
for line in tqdm.tqdm(data):
    matcher = NodeMatcher(graph)
    node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()

    if node != None:
        continue
    sum += 1
    node = Node('{node_class}'.format(node_class=line[3]),name='{name}'.format(name=line[0]),color='{col}'.format(col=line[1]),features='{fea}'.format(fea=line[2]))
    graph.create(node)
print('created %d nodes' % sum)
