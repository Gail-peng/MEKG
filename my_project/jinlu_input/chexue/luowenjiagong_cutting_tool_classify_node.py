from py2neo import *
import pandas as pd
import numpy as np
import tqdm


graph = Graph('http://localhost:7474',password = '123456')
file = pd.read_excel('data/螺纹刀杆分类.xlsx')
data = np.array(file)
data = data.tolist()

# sum = 0
# for line in tqdm.tqdm(data):
#     matcher = NodeMatcher(graph)
#     node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()
#
#     if node != None:
#         continue
#     sum += 1
#     node = Node('{node_class}'.format(node_class=line[2]),
#                 name='{name}'.format(name=line[0]),
#                 features='{fea}'.format(fea=line[1]))
#     graph.create(node)
# print('created %d nodes' % sum)
#
# graph = Graph('http://localhost:7474',password = '123456')
# file = pd.read_excel('data/螺纹刀片分类.xlsx')
# data = np.array(file)
# data = data.tolist()

sum = 0
for line in tqdm.tqdm(data):
    matcher = NodeMatcher(graph)
    node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()

    if node != None:
        continue
    sum += 1
    node = Node('{node_class}'.format(node_class=line[1]),
                name='{name}'.format(name=line[0]),
                fac='{fac}'.format(fac=line[2]))
    graph.create(node)
print('created %d nodes' % sum)