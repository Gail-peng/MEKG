import os
import pandas as pd
from py2neo import *
import tqdm
graph = Graph('http://localhost:7474',password = '123456')

def get_file():
    read_path = './shangao_input/params/node'
    return read_path

def createnode(header,vals):
    ex = []
    heads = header
    for head in heads:   #获取节点属性中的class属性
        if head == 'class':
            class_index = heads.index(head)   #得到class的索引值
    sum = 0
    for val in tqdm.tqdm(vals):
        matcher = NodeMatcher(graph)
        node = matcher.match(name='{node_name}'.format(node_name=val[0])).first()   #根据名称索引节点信息
        if node != None:   #如果节点存在，那么就不创建新的了
            ex.append(('节点 '+val[0]+' 已经存在'))
            continue
        sum = sum + 1
        node = Node('{node_class}'.format(node_class=val[class_index]),
                    name='{name}'.format(name=val[0]))   #创建根据class和name创建节点
        graph.create(node)  #将创建的节点加入数据库
    print('created %d nodes' % sum,ex)


def createnode_properties(header,vals):
    head_count = header[:]  #获得对应属性的索引值
    header = header[1:]     #因为创建节点的时候已经输入名字了，因此第一项不考虑
    for head in header:
        if head == 'class':   #排除class属性
            continue
        print('更新属性： ' + head)
        sum = 0
        for val in tqdm.tqdm(vals):    #得到每一个节点的属性值表格
            sum += 1
            matcher = NodeMatcher(graph)
            node = matcher.match(name='{node_name}'.format(node_name=val[0])).first()   #根据名称索引相应的节点
            node[head] = val[head_count.index(head)]   #更新属性值
            graph.push(node)  #将更新值加入数据库中
        print('updated %d nodes' % sum)



def read_file(datas):
    files = os.listdir(read_path)  #得到路径下所有的文件名称
    for file_name in files:
        if file_name[-2:] == 'sx':   #如果不是excell文件，不会执行下面的程序
            data = pd.read_excel(read_path+'/'+file_name)  #打开每个文件
            get_data = []  #建立一个list，用于存储节点属性的list和节点属性值的list
            data_header = data.columns.tolist()   #获得节点属性list
            data = data.values.tolist()     #获得节点属性值list
            get_data.append(data_header)   #节点属性list加入get_data
            get_data.append(data)     #节点属性值list加入get_data
            get_data.append(file_name)  #文件名称加入get_data
            datas.append(get_data)  #将get_data放进datas中，下一步用


if __name__ == '__main__':
    datas = []
    read_path = get_file()
    read_file(datas)
    for data in datas:  #创建节点的for循环
        print('file ' + data[2] + ' has opened')
        createnode(data[0],data[1])
    for data in datas:  #索引每一个文件的list表，data【0】为节点的属性，data【1】为属性值，data【2】为文件名称
        print('file ' + data[2] + ' has opened')
        createnode_properties(data[0],data[1])


