from py2neo import *
import pandas as pd
import numpy as np
import tqdm
graph = Graph('http://localhost:7474',password = '123456')
file = pd.read_excel('data/螺纹加工刀片.xlsx')
data = np.array(file)
data = data.tolist()
# sum = 0
# for line in tqdm.tqdm(data):
#     matcher = NodeMatcher(graph)
#     node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()
#
#     if node != None:
#         continue
#     sum = sum+1
#     node = Node('{node_class}'.format(node_class=line[10]),
#                 name='{name}'.format(name=line[0]),
#                 PDY='{pd}'.format(pd=line[1]),
#                 PDX='{dx}'.format(dx=line[2]),
#                 RE='{re}'.format(re=line[3]),
#                 IC='{ic}'.format(ic=line[4]),
#                 S='{s}'.format(s=line[5]),
#                 D1='{d1}'.format(d1=line[6]),
#                 PITCH='{p}'.format(p=line[7]),
#                 feature='{fea}'.format(fea=line[9]),
#                 tool_type='{toolty}'.format(toolty=line[11]),
#                 factory = '{fac}'.format(fac=line[8])
#                 )
#     graph.create(node)
# print('created %d nodes'%sum)


# file = pd.read_excel('data/螺纹加工刀杆.xlsx')
# data = np.array(file)
# data = data.tolist()
# sum = 0
# for line in tqdm.tqdm(data):
#     matcher = NodeMatcher(graph)
#     node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()
#
#     if node != None:
#         continue
#     sum = sum+1
#     node = Node('{node_class}'.format(node_class=line[7]),
#                 name='{name}'.format(name=line[0]),
#                 H='{h}'.format(h=line[1]),
#                 B='{b}'.format(b=line[2]),
#                 LF='{lf}'.format(lf=line[3]),
#                 WF='{wf}'.format(wf=line[4]),
#                 HF='{hf}'.format(hf=line[5]),
#                 OHX='{ohx}'.format(ohx=line[6]),
#                 tool_type='{toolty}'.format(toolty=line[8]),
#                 factory = '{fac}'.format(fac=line[9])
#                 )
#     graph.create(node)
# print('created %d nodes'%sum)


file = pd.read_excel('data/螺纹加工刀杆1.xlsx')
data = np.array(file)
data = data.tolist()
sum = 0
for line in tqdm.tqdm(data):
    matcher = NodeMatcher(graph)
    node = matcher.match(name='{node_name}'.format(node_name = line[0])).first()

    if node != None:
        continue
    sum = sum+1
    node = Node('{node_class}'.format(node_class=line[7]),
                name='{name}'.format(name=line[0]),
                DMIN1='{dm}'.format(dm=line[1]),
                DCON='{dc}'.format(dc=line[2]),
                H='{h}'.format(h=line[3]),
                WF='{wf}'.format(wf=line[5]),
                LF='{lf}'.format(lf=line[4]),
                OHN='{oh}'.format(oh=line[6]),
                tool_type='{toolty}'.format(toolty=line[8]),
                factory = '{fac}'.format(fac=line[9])
                )
#     graph.create(node)
# print('created %d nodes'%sum)

