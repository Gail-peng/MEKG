from py2neo import *
import pandas as pd
import numpy as np
import tqdm
graph = Graph('http://localhost:7474',password = '123456')
file = pd.read_excel('data/切断切槽刀片1.xlsx')
data = np.array(file)
data = data.tolist()
sum = 0
for line in tqdm.tqdm(data):
    matcher = NodeMatcher(graph)
    node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()

    if node != None:
        continue
    sum = sum+1
    # node = Node('{node_class}'.format(node_class=line[8]),
    #             name='{name}'.format(name=line[0]),
    #             CW='{cw}'.format(cw=line[1]),
    #             RE='{re}'.format(re=line[2]),
    #             L='{l}'.format(l=line[3]),
    #             W1='{w1}'.format(w1=line[4]),
    #             S='{s}'.format(s=line[5]),
    #             factory='{fac}'.format(fac=line[6]),
    #             feature='{fea}'.format(fea=line[7]),
    #             tool_type='{toolty}'.format(toolty=line[9])
    #             )

    node = Node('{node_class}'.format(node_class=line[9]),
                name='{name}'.format(name=line[0]),
                CW='{cw}'.format(cw=line[1]),
                CDX='{cdx}'.format(cdx=line[2]),
                RE='{re}'.format(re=line[3]),
                IC='{ic}'.format(ic=line[4]),
                W1='{w1}'.format(w1=line[5]),
                D1='{d1}'.format(d1=line[6]),
                factory='{fac}'.format(fac=line[7]),
                feature='{fea}'.format(fea=line[8]),
                tool_type='{toolty}'.format(toolty=line[10])
                )
    graph.create(node)
print('created %d nodes'%sum)
