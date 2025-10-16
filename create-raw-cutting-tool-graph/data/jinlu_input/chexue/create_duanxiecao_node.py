from py2neo import *
import pandas as pd
import numpy as np
import tqdm


graph = Graph('http://localhost:7474',password = '123456')
file = pd.read_excel('data/duanxiecao.xlsx')
data = np.array(file)
data = data.tolist()

for line in tqdm.tqdm(data):

    matcher = NodeMatcher(graph)
    node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()

    if node != None:
        continue
    node = Node('{node_class}'.format(node_class=line[2]),name='{name}'.format(name=line[0]),features='{fea}'.format(fea=line[1]))
    graph.create(node)