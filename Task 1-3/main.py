import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def create_and_visualize_network():
    G = nx.Graph()

    nodes = ["Train station", "Bus station", "Mall", "Park", "Market", "University", "Hospital"]
    G.add_nodes_from(nodes)

    edges = [("Train station", "Bus station", 5), ("Train station", "Mall", 2), ("Bus station", "Park", 1), 
             ("Mall", "Market", 4), ("Park", "Market", 6), ("Market", "University", 2), ("University", "Hospital", 3)]
    G.add_weighted_edges_from(edges)

    plt.figure(figsize=(10, 7))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', linewidths=2, font_size=15, font_weight='bold')

    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degrees = G.degree()

    print(f"Nodes: {num_nodes}")
    print(f"Edges: {num_edges}")
    print("Degree:")
    for node, degree in degrees:
        print(f"{node}: {degree}")
    
    print(f"--------")
    dfs_path = dfs(G, "Bus station", "Hospital")
    bfs_path = bfs(G, "Bus station", "Hospital")

    print("DFS path: " + str(dfs_path))
    print("BFS path: " + str(bfs_path))
    print(f"--------")

    distances = dijkstra(G, "Bus station")
    print(f"Distances from 'Bus station': {distances}")

    plt.show()

def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    vertices = list(graph.nodes)

    while vertices:
        current_vertex = min(vertices, key=lambda vertex: distances[vertex])
        vertices.remove(current_vertex)
        
        for neighbor in graph[current_vertex]:
            edge_weight = graph[current_vertex][neighbor]['weight']
            alternative_route = distances[current_vertex] + edge_weight
            
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route

    return distances

if __name__ == "__main__":
    create_and_visualize_network()
