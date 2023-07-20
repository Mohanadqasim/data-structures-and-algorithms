# Graph Business Trip

## Problem domain

Write the following method for the Graph class:

    Arguments: graph, array of city names
    Return: the cost of the trip (if it’s possible) or null (if not)

## Code 

```py

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
```

## Approach & Efficiency

- Space complexity: O(V)
- Time complexity: O(N)

> V is the number of vertices (cities) in the graph and N is the number of cities in the input list.