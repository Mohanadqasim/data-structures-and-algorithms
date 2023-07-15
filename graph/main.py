from graph import Graph

graph1 = Graph()

a = graph1.add_vertex("A")
b = graph1.add_vertex("B")
c = graph1.add_vertex("C")
d = graph1.add_vertex("D")

graph1.add_edge(a,b)
graph1.add_edge(a,c)
graph1.add_edge(c,b)
graph1.add_edge(d,b)
graph1.add_edge(d,c)

print(graph1.get_vertice())