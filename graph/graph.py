class Node:
    def __init__(self,value=None):
        self.value = value

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self,value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex
    
    def add_edge(self,vertex1,vertex2,weight=0):
        if not vertex1 or not vertex2 in self.adj_list.keys():
            return('this vertex does not exist')
        
        edge1 = Edge(vertex2,weight)
        self.adj_list[vertex1].append(edge1)

        edge2 = Edge(vertex1,weight)
        self.adj_list[vertex2].append(edge2)

    def get_vertice(self):
        return self.adj_list.keys()
    
    def get_neighbors(self, vertex):
        return self.adj_list[vertex]
    
    def size(self):
        if len(self.adj_list.keys()) == 0:
            return None
        return len(self.adj_list.keys())