from py2neo import *
import pandas as pd
import numpy as np
import tqdm


graph = Graph('http://localhost:7474',password = '123456')
file = pd.read_excel('data/切断切槽断屑槽.xlsx')
data = np.array(file)
data = data.tolist()

sum = 0
for i in tqdm.tqdm(data):
    matcher = NodeMatcher(graph)

    node = matcher.match('{node_class}'.format(node_class=i[3])).where(name='{name}'.format(name = i[0])).first()
    if node != None:
        continue
    sum += 1
    node = Node('{node_class}'.format(node_class=i[3]),
                name='{name}'.format(name=i[0]),
                type = '{ty}'.format(ty = i[1]),
                wide = '{wi}'.format(wi = i[2]))
    graph.create(node)
print('created %d nodes' % sum)
