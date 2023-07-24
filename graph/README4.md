# Graph Depth first

## Problem domain

Write the following method for the Graph class:

    Name: Depth first
    Arguments: Node (Starting point of search)
    Return: A collection of nodes in their pre-order depth-first traversal order
    Program output: Display the collection


## Code 

```py
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
```

## Approach & Efficiency

- Space complexity: O(V)
- Time complexity: O(V + E) 

> V is the number of vertices (nodes) and E is the number of edges in the graph.