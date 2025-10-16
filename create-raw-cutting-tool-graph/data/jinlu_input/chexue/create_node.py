from py2neo import *
import pandas as pd
import numpy as np
import tqdm


graph = Graph('http://localhost:7474',password = '123456')
file = pd.read_excel('data/root_node.xlsx')
data = np.array(file)
data = data.tolist()

sum = 0
for i in tqdm.tqdm(data):
    matcher = NodeMatcher(graph)

    node = matcher.match('{node_class}'.format(node_class=i[0])).where(name='{name}'.format(name = i[1])).first()
    if node != None:
        continue
    sum += 1
    node = Node('{node_class}'.format(node_class=i[0]),name='{name}'.format(name=i[1]))
    graph.create(node)
print('created %d nodes' % sum)




