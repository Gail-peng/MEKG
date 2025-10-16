from py2neo import *
import numpy as np


graph = Graph('http://localhost:7474',password = '123456')

search = graph.run("match(n)-[r:材料是]->(m) where n.name ='CNMG120408-QM'  return (n)").to_series()
for i in search:

    print(i)
