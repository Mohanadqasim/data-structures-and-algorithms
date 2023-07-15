# Graph
## Problem domain

Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

    add vertex
        Arguments: value
        Returns: The added vertex
        Add a vertex to the graph
    add edge
        Arguments: 2 vertices to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph
    get vertices
        Arguments: none
        Returns all of the vertices in the graph as a collection (set, list, or similar)
        Empty collection returned if there are no vertices
    get neighbors
        Arguments: vertex
        Returns a collection of edges connected to the given vertex
            Include the weight of the connection in the returned collection
        Empty collection returned if there are no vertices
    size
        Arguments: none
        Returns the total number of vertices in the graph
        0 if there are none

## Code 

```python 
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
```

## Approach & Efficiency
- add_vertex: O(1)
- add_edge: O(1)
- get_vertice: O(n)
- get_neighbors: O(1)
- size: O(1)