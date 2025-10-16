import json
from py2neo import Graph, Node, Relationship, NodeMatcher,RelationshipMatcher

class CreateRel:
    def __init__(self,graph:Graph,file_path:str):
        self.graph = graph
        self.matcher = NodeMatcher(graph)
        self.rel_matcher = RelationshipMatcher(graph)
        self.data_dir = file_path

    def create_rel(self):
        with open(self.data_dir, 'r') as f:
            rels = json.loads(f.read())['relationships']
            for rel in rels:
                rel_type = rel['type']  # 避免使用内置关键字type
                # 获取头节点和尾节点
                node_head = self.matcher.match(id=rel['start']).first()
                node_tail = self.matcher.match(id=rel['end']).first()

                # 跳过节点不存在的情况
                if not node_head or not node_tail:
                    print(f"节点不存在（{rel['start']} 或 {rel['end']}），跳过关系")
                    continue

                # 检查关系是否已存在：匹配从head到tail的指定类型关系
                # rel_matcher.match()会返回所有符合条件的关系（可迭代对象）
                existing_rel = self.rel_matcher.match(
                    start_node=node_head,
                    end_node=node_tail,
                    r_type=rel_type
                ).first()  # 取第一个匹配的关系（若存在）

                if not existing_rel:
                    # 关系不存在，创建并保存
                    new_relation = Relationship(node_head, rel_type, node_tail)
                    self.graph.create(new_relation)
                    print(f"创建关系：{node_head['id']} -[{rel_type}]-> {node_tail['id']}")
                else:
                    # 关系已存在，跳过
                    print(f"关系已存在，跳过：{node_head['id']} -[{rel_type}]-> {node_tail['id']}")