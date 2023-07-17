import pytest
from graph import Graph, Edge, Node

@pytest.fixture
def graph():
    # Create a new graph
    graph = Graph()
    
    # Add vertices
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    vertex3 = graph.add_vertex(3)
    
    # Add edges
    graph.add_edge(vertex1, vertex2, 10)
    graph.add_edge(vertex2, vertex3, 5)
    
    return graph

def test_add_vertex(graph):
    vertex4 = graph.add_vertex(4)
    vertices = graph.get_vertice()
    assert vertex4 in vertices

def test_add_edge(graph):
    vertex4 = graph.add_vertex(4)
    vertex5 = graph.add_vertex(5)
    graph.add_edge(vertex4, vertex5, 7)
    neighbors = graph.get_neighbors(vertex4)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == vertex5
    assert neighbors[0].weight == 7

def test_add_multiple_edges(graph):
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)

    graph.add_edge(vertex1, vertex2, 5)
    graph.add_edge(vertex1, vertex2, 10)
    graph.add_edge(vertex1, vertex2, 7)

    neighbors = graph.get_neighbors(vertex1)
    assert len(neighbors) == 3
    weights = [edge.weight for edge in neighbors]
    assert set(weights) == {5, 10, 7}

def test_add_edges_different_vertices(graph):
    vertex1 = graph.add_vertex(1)
    vertex2 = graph.add_vertex(2)
    vertex3 = graph.add_vertex(3)

    graph.add_edge(vertex1, vertex2, 5)
    graph.add_edge(vertex1, vertex3, 10)
    
    assert len(graph.get_neighbors(vertex1)) == 2
    assert len(graph.get_neighbors(vertex2)) == 1
    assert len(graph.get_neighbors(vertex3)) == 1



def test_get_neighbors_with_weight(graph):
    vertex2 = list(graph.get_vertice())[1]
    neighbors = graph.get_neighbors(vertex2)
    assert neighbors[0].weight == 10 or neighbors[1].weight == 10
    assert neighbors[0].weight == 5 or neighbors[1].weight == 5

def test_get_neighbors_no_edges(graph):
    vertex = graph.add_vertex(1)
    neighbors = graph.get_neighbors(vertex)
    assert len(neighbors) == 0

def test_get_vertices_empty_graph():
    empty_graph = Graph()
    vertices = empty_graph.get_vertice()
    assert len(vertices) == 0

def test_size(graph):
    size = graph.size()
    assert size == 3

def test_single_vertex_graph():
    graph = Graph()
    vertex = graph.add_vertex(1)
    vertices = list(graph.get_vertice())
    assert len(vertices) == 1
    assert vertices[0] == vertex

def test_breadth_first(graph):
    result = graph.breadth_first(list(graph.get_vertice())[0])
    assert len(result) == 3
    assert result == list(graph.get_vertice())

def test_breadth_first_invalid_start_node(graph):
    result = graph.breadth_first(Node(4))
    assert len(result) == 0

if __name__ == "__main__":
    pytest.main()

if __name__ == "__main__":
    pytest.main()
