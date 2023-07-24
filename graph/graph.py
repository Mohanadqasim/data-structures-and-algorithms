from collections import deque
class Node:
    def __init__(self,value=None):
        self.value = value

    def __repr__(self):
        return str(self.value)

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight
    
    def __repr__(self):
        return f"vertex: {self.vertex}, weight: {self.weight}"

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
    


    def breadth_first(self, start_node):
        visited = set()  
        queue = deque()  
        result = []  

        if start_node not in self.adj_list:
            print("Invalid start node.")
            return result

        queue.append(start_node)
        visited.add(start_node)

        while queue:
            node = queue.popleft()
            result.append(node)

            neighbors = self.adj_list[node]
            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        for node in result:
            print(node.value)

        return result
    


    def business_trip(self, cities):
        price = 0
        for i in range(len(cities) - 1):
            current_city = cities[i]
            next_city = cities[i + 1]
            found_next_city = False

            neighbors = self.get_neighbors(current_city)
            
            for idx, direction in enumerate(neighbors):
                if direction.vertex == next_city:
                    price += neighbors[idx].weight
                    found_next_city = True
            
            if not found_next_city:
                return 'Null'

        return price


    def depth_first(self, start_node):
        if start_node not in self.adj_list:
            print("Invalid start node.")
            return []

        visited = set()
        stack = deque([start_node])
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)

                neighbors = reversed(self.adj_list[node]) 
                for edge in neighbors:
                    neighbor = edge.vertex
                    if neighbor not in visited:
                        stack.append(neighbor)

        for node in result:
            print(node.value)

        return result
    

    def __repr__(self):
        output = ''
        for vertex in self.adj_list:
            output += f'{vertex.__str__()} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.__str__()} / '
            output += '\n'
        return output

