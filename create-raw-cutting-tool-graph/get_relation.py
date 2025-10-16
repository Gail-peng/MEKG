import pandas as pd
from py2neo import *
import numpy as py
from tqdm import tqdm
import os

graph = Graph('http://localhost:7474',password = '123456')

def get_readfiles(read_path,datas):
    files = os.listdir(read_path)
    for file_name in files:
        if file_name[-1] == 'x':  # 如果不是excell文件，不会执行下面的程序
            data = pd.read_excel(read_path + '/' + file_name)  # 打开每个文件
            get_data = []  # 建立一个list，用于存储节点属性的list和节点属性值的list
            data = data.values.tolist()  # 获得节点属性值list
            get_data.append(data)  # 节点属性值list加入get_data
            get_data.append(file_name)  # 文件名称加入get_data
            datas.append(get_data)  # 将get_data放进datas中，下一步用

def create_relation(vals):
    sum = 0
    for val in tqdm(vals):
        node_head = graph.nodes.match().where(name='{name}'.format(name=val[0])).first()
        node_tail = graph.nodes.match().where(name='{name}'.format(name=val[2])).first()
        matcher = RelationshipMatcher(graph)
        relation = matcher.match((node_head, node_tail), r_type='{rel}'.format(rel=val[1])).first()
        if relation != None:
            continue
        sum = sum + 1
        r = Relationship(node_head, '{rel}'.format(rel=val[1]), node_tail)
        graph.create(r)
    print('created %d relations' % sum)


if __name__ == '__main__':
    read_path = './shangao_input/params/relation'
    datas = []
    get_readfiles(read_path,datas)
    for data in datas:
        print('file ' + data[1] + ' has opened')
        create_relation(data[0])

