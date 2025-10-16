from py2neo import *
import pandas as pd
import numpy as np
import tqdm
graph = Graph('http://localhost:7474',password = '123456')
file = pd.read_excel('data/车削刀杆.xlsx')
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
                H='{le}'.format(le=line[1]),
                B='{ic}'.format(ic=line[2]),
                LF='{s}'.format(s=line[3]),
                OHX='{d1}'.format(d1=line[4]),
                HF='{re}'.format(re=line[5]),
                WF='{fac}'.format(fac=line[6]),
                type='{ty}'.format(ty=line[8]),
                angle='{ang}'.format(ang=line[7]),
                tool_type='{toolty}'.format(toolty=line[10]),
                factory = '{fac}'.format(fac=line[11])
                )
    graph.create(node)
print('created %d nodes'%sum)