from py2neo import *
import pandas as pd
import numpy as np
import tqdm
graph = Graph('http://localhost:7474',password = '123456')
file = pd.read_excel('data/内孔车刀杆.xlsx')
data = np.array(file)
data = data.tolist()
sum = 0
for line in tqdm.tqdm(data):
    matcher = NodeMatcher(graph)
    node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()

    if node != None:
        continue
    sum = sum+1
    node = Node('{node_class}'.format(node_class=line[9]),
                name='{name}'.format(name=line[0]),
                Dmin1='{d}'.format(d=line[1]),
                Dcon='{dc}'.format(dc=line[2]),
                WF='{wf}'.format(wf=line[3]),
                LF='{lf}'.format(lf=line[4]),
                OHN='{ohn}'.format(ohn=line[5]),
                H='{h}'.format(h=line[6]),
                A='{a}'.format(a=line[7]),
                angle='{ang}'.format(ang=line[8]),
                tool_type='{toolty}'.format(toolty=line[10]),
                factory = '{fac}'.format(fac=line[11])
                )
    graph.create(node)
print('created %d nodes'%sum)