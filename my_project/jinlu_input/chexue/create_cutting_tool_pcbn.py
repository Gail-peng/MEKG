import numpy as np
import tqdm
from py2neo import *
import pandas as pd
graph = Graph('http://localhost:7474',password = '123456')
file = pd.read_excel('data/pcbn刀片1.xlsx')
data = np.array(file)
data = data.tolist()
sum = 0
for line in tqdm.tqdm(data):
    matcher = NodeMatcher(graph)
    node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()

    if node != None:
        continue
    sum = sum+1
    # node = Node('{node_class}'.format(node_class=line[9]),
    #             name='{name}'.format(name=line[0]),
    #             LE='{le}'.format(le=line[1]),
    #             IC='{ic}'.format(ic=line[2]),
    #             S='{s}'.format(s=line[3]),
    #             D1='{d1}'.format(d1=line[4]),
    #             RE='{re}'.format(re=line[5]),
    #             factory='{fac}'.format(fac=line[6]),
    #             feature='{fea}'.format(fea=line[7]),
    #             type='{ty}'.format(ty=line[8]),
    #             tool_type='{toolty}'.format(toolty=line[10]),
    #             Number_of_blades = '{nob}'.format(nob=line[11])
    #             )
    # graph.create(node)

    node = Node('{node_class}'.format(node_class=line[7]),
                name='{name}'.format(name=line[0]),

                IC='{ic}'.format(ic=line[1]),
                S='{s}'.format(s=line[2]),
                D1='{d1}'.format(d1=line[3]),

                factory='{fac}'.format(fac=line[4]),
                feature='{fea}'.format(fea=line[5]),
                type='{ty}'.format(ty=line[6]),
                tool_type='{toolty}'.format(toolty=line[8]),
                Number_of_blades='{nob}'.format(nob=line[9])
                )
    graph.create(node)
print('created %d nodes'%sum)