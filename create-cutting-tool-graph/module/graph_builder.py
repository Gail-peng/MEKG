from module.connection import CreateConnection
from module.node2graph import CreateNode
from module.rel2graph import CreateRel
import json

class GraphBuilder:
    def __init__(self):
        with open('./config/config.json', 'r') as f:
            config_data = json.load(f)
            self.url = config_data['url']
            self.file_path = config_data['file_path']
            self.user = config_data['user']
            self.password = config_data['password']
    def build_graph(self):
        graph = CreateConnection(self.url,self.user,self.password).create_connection()
        CreateNode(graph,self.file_path).create_node()
        CreateRel(graph,self.file_path).create_rel()