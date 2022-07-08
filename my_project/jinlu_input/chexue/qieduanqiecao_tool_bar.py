from py2neo import *
import pandas as pd
import numpy as np
import tqdm
#第一种刀具类型
# graph = Graph('http://localhost:7474',password = '123456')
# file = pd.read_excel('data/切断切槽刀杆.xlsx')
# data = np.array(file)
# data = data.tolist()
# sum = 0
# for line in tqdm.tqdm(data):
#     matcher = NodeMatcher(graph)
#     node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()
#     if node != None:
#         continue
#     sum = sum+1
#     node = Node('{node_class}'.format(node_class=line[8]),
#                 name='{name}'.format(name=line[0]),
#                 W='{w}'.format(w=line[1]),
#                 CDX='{cdx}'.format(cdx=line[2]),
#                 HF='{hf}'.format(hf=line[3]),
#                 B='{b}'.format(b=line[4]),
#                 LF='{lf}'.format(lf=line[5]),
#                 WF='{wf}'.format(wf=line[6]),
#                 factory='{fac}'.format(fac=line[10]),
#                 mf_type='{mt}'.format(mt=line[7]),
#                 tool_type='{toolty}'.format(toolty=line[9])
#                 )
#     graph.create(node)
# print('created %d nodes' % sum)

#表2的内容
# graph = Graph('http://localhost:7474',password = '123456')
# file = pd.read_excel('data/切断切槽刀杆2.xlsx')
# data = np.array(file)
# data = data.tolist()
# sum = 0
# for line in tqdm.tqdm(data):
#     matcher = NodeMatcher(graph)
#     node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()
#     if node != None:
#         continue
#     sum = sum+1
#     node = Node('{node_class}'.format(node_class=line[9]),
#                 name='{name}'.format(name=line[0]),
#                 H='{h}'.format(h=line[1]),
#                 B='{b}'.format(b=line[2]),
#                 LF='{lf}'.format(lf=line[3]),
#                 WF='{wf}'.format(wf=line[4]),
#                 CDX='{cd}'.format(cd=line[5]),
#                 DMIN1='{dm}'.format(dm=line[6]),
#                 DMAX1='{dmx}'.format(dmx=line[7]),
#                 factory='{fac}'.format(fac=line[11]),
#                 mf_type='{mt}'.format(mt=line[8]),
#                 tool_type='{toolty}'.format(toolty=line[10])
#                 )
#     graph.create(node)
# print('created %d nodes' % sum)

#表1的内容
# graph = Graph('http://localhost:7474',password = '123456')
# file = pd.read_excel('data/切断切槽刀杆1.xlsx')
# data = np.array(file)
# data = data.tolist()
# sum = 0
# for line in tqdm.tqdm(data):
#     matcher = NodeMatcher(graph)
#     node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()
#     if node != None:
#         continue
#     sum = sum+1
#     node = Node('{node_class}'.format(node_class=line[10]),
#                 name='{name}'.format(name=line[0]),
#                 W='{w}'.format(w=line[1]),
#                 CD1='{cd}'.format(cd=line[2]),
#                 DMIN1='{dm1}'.format(dm1=line[3]),
#                 DCON='{dcon}'.format(dcon=line[4]),
#                 WF='{wf}'.format(wf=line[5]),
#                 LF='{lf}'.format(lf=line[6]),
#                 OHN='{ohn}'.format(ohn=line[7]),
#                 H='{h}'.format(h=line[8]),
#                 factory='{fac}'.format(fac=line[12]),
#                 mf_type='{mt}'.format(mt=line[9]),
#                 tool_type='{toolty}'.format(toolty=line[11])
#                 )
#     graph.create(node)
# print('created %d nodes' % sum)

#表3的内容
# graph = Graph('http://localhost:7474',password = '123456')
# file = pd.read_excel('data/切断切槽刀杆3.xlsx')
# data = np.array(file)
# data = data.tolist()
# sum = 0
# for line in tqdm.tqdm(data):
#     matcher = NodeMatcher(graph)
#     node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()
#     if node != None:
#         continue
#     sum = sum+1
#     node = Node('{node_class}'.format(node_class=line[8]),
#                 name='{name}'.format(name=line[0]),
#                 H='{h}'.format(h=line[1]),
#                 B='{b}'.format(b=line[2]),
#                 WF='{wf}'.format(wf=line[4]),
#                 LF='{lf}'.format(lf=line[3]),
#                 A='{a}'.format(a=line[5]),
#                 CDX='{cdx}'.format(cdx=line[6]),
#                 factory='{fac}'.format(fac=line[10]),
#                 mf_type='{mt}'.format(mt=line[7]),
#                 tool_type='{toolty}'.format(toolty=line[9])
#                 )
#     graph.create(node)
# print('created %d nodes' % sum)

#表4的内容
graph = Graph('http://localhost:7474',password = '123456')
file = pd.read_excel('data/切断切槽刀杆4.xlsx')
data = np.array(file)
data = data.tolist()
sum = 0
for line in tqdm.tqdm(data):
    matcher = NodeMatcher(graph)
    node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()
    if node != None:
        continue
    sum = sum+1
    node = Node('{node_class}'.format(node_class=line[8]),
                name='{name}'.format(name=line[0]),
                DMIN1='{dm1}'.format(dm1=line[1]),
                DCON='{dcon}'.format(dcon=line[2]),
                H='{h}'.format(h=line[3]),
                WF='{wf}'.format(wf=line[5]),
                LF='{lf}'.format(lf=line[4]),
                CDX='{cdx}'.format(cdx=line[6]),
                factory='{fac}'.format(fac=line[10]),
                mf_type='{mt}'.format(mt=line[7]),
                tool_type='{toolty}'.format(toolty=line[9])
                )
    graph.create(node)
print('created %d nodes' % sum)