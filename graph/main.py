from graph import Graph
# list=["Arendelle", "New Monstropolis", "Naboo"]
graph1 = Graph()

a = graph1.add_vertex("Arendelle")
b = graph1.add_vertex("New Monstropolis")
c = graph1.add_vertex("Naboo")
d = graph1.add_vertex("Amman")
e = graph1.add_vertex("Irbid")

graph1.add_edge(a,b,800)
graph1.add_edge(b,c,500)
graph1.add_edge(c,d,1500)


print(graph1.get_neighbors(a))
# print(type(graph1.get_neighbors(a)))
print(graph1.business_trip([a,b,c,d,e]))