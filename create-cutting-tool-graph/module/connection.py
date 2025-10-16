from py2neo import Graph,NodeMatcher

class CreateConnection:
    def __init__(self,url:str,user:str,password:str):
        self.url = url
        self.user = user
        self.password = password

    def create_connection(self) -> Graph:
        graph = Graph(self.url, user=self.user, password=self.password)
        return graph
