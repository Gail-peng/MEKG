import json
from py2neo import Graph, Node, Relationship, NodeMatcher

class CreateNode:
    def __init__(self,graph:Graph,file_path:str):
        self.graph = graph
        self.matcher = NodeMatcher(graph)
        self.node_id_list = []
        self.data_dir = file_path

    def create_node(self):
        # create node in neo4j
        with open(self.data_dir,'r') as f:
            nodes = json.loads(f.read())['nodes']
            for data in nodes:
                label = data['labels'][0]
                del data['labels']
                # print(label,data)
                if data['id'] not in self.node_id_list:
                    node = self.matcher.match(id=data['id']).first()
                    if node == None:
                        self.node_id_list.append(data['id'])
                        node = Node(label,**data)
                        self.graph.create(node)
                        print(f"节点不存在（id:{data['id']},名称:{data['name']}），创建节点")
                    else:
                        print(f"节点已存在（id:{data['id']},名称:{data['name']}），跳过节点创建")