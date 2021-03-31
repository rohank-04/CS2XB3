import lab9
import min_heap
import random
import matplotlib.pyplot as plt
import time


def bellman_ford_approx(G, source, k):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    nodes = list(G.adj.keys())

    # Initialize distances
    for node in nodes:
        dist[node] = 99999
    dist[source] = 0

    # Meat of the algorithm
    for _ in range(k):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist


def bellman_ford_perfect(G, source):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    nodes = list(G.adj.keys())

    # Initialize distances
    for node in nodes:
        dist[node] = 99999
    dist[source] = 0

    # Meat of the algorithm
    for i in range(G.number_of_nodes()):
        if i % 5 == 0:
            prevDist = lab9.total_dist(dist)

        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
        if i % 5 == 4:
            newDist = lab9.total_dist(dist)
            if newDist == prevDist:
                return dist
    return dist


def all_pairs_dijkstra(G):
    shortestPaths = []
    for i in range(G.number_of_nodes()):
        currShortestPath = []
        x = lab9.dijkstra(G, i)
        for j in x.keys():
            currShortestPath.append(x[j])
        shortestPaths.append(currShortestPath)

    return shortestPaths


def all_pairs_bellman_ford(G):
    shortestPaths = []
    for i in range(G.number_of_nodes()):
        currShortestPath = []
        x = lab9.bellman_ford(G, i)
        for j in x.keys():
            currShortestPath.append(x[j])
        shortestPaths.append(currShortestPath)

    return shortestPaths


# G = create_random_complete_graph_negative(4, 10)
# # print(G.adj)
# print(G.weights)


# # # print(all_pairs_dijkstra(G))

# print("")
# print("")
# print("")
# h = DirectedWeightedGraph()
# h.add_node(0)
# h.add_node(1)
# h.add_node(2)
# h.add_node(3)
# h.add_node(4)

# h.add_edge(0, 1, -1)
# h.add_edge(0, 2, 4)
# h.add_edge(1, 2, 3)
# h.add_edge(1, 3, 2)
# h.add_edge(1, 4, 2)
# h.add_edge(3, 2, 5)
# h.add_edge(3, 1, 1)
# h.add_edge(4, 3, -3)
# print(bellman_ford(h, 1))
# print("")
# print("")
# print("")
# print(mystery(h))
# print("")
# print("")
# print("")
# print(all_pairs_bellman_ford(h))
