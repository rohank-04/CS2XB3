from lab7 import Graph, DFS, BFS
from collections import deque

# Breadth First Search


def BFS2(G, node1, node2):
    Q = deque([node1])
    path = {}
    for node in G.adj:
        path[node] = -1

    path[node1] = node1
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                path[node] = current_node
                ans = [node2]
                while node2 != node1:
                    node2 = path[node2]
                    ans.insert(0, node2)
                return ans
            if path[node] == -1:
                path[node] = current_node
                Q.append(node)
    return []


def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    path = {}
    for node in G.adj:
        marked[node] = False
        path[node] = -1

    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:

                if node == node2:
                    path[node] = current_node
                    end = node2
                    start = node1
                    accPath = [end]
                    while end != start:
                        newEnd = path[end]
                        accPath.insert(0, newEnd)
                        end = newEnd
                    return accPath

                if path[node] == -1:
                    path[node] = current_node
                    S.append(node)
    return []


def DFS3(graph, node1):
    graphLength = len(graph.adj)
    paths = {}
    for i in range(graphLength):
        if i != node1:
            paths[i] = -1

    for i in paths:
        if paths[i] == -1:
            currPath = DFS2(graph, node1, i)
            if currPath != []:
                currPath.reverse()
                for i in range(len(currPath)-1):
                    if paths[currPath[i]] == -1:
                        paths[currPath[i]] = currPath[i+1]

    toBeDeleted = []
    for i in paths:
        if paths[i] == -1:
            toBeDeleted.append(i)
    for i in toBeDeleted:
        del paths[i]
    return(paths)


def BFS3(graph, node1):
    graphLength = len(graph.adj)
    paths = {}
    for i in range(graphLength):
        if i != node1:
            paths[i] = -1

    for i in paths:
        if paths[i] == -1:
            currPath = BFS2(graph, node1, i)
            if currPath != []:
                currPath.reverse()
                for i in range(len(currPath)-1):
                    if paths[currPath[i]] == -1:
                        paths[currPath[i]] = currPath[i+1]

    toBeDeleted = []
    for i in paths:
        if paths[i] == -1:
            toBeDeleted.append(i)
    for i in toBeDeleted:
        del paths[i]
    return(paths)


def has_cycle(graph):
    marked = {}
    cycleFound = [False]
    for node in graph.adj:
        marked[node] = False

    for node in graph.adj:
        if marked[node] == False:
            hasCycleHelper(graph, node, cycleFound, node, marked)
        if cycleFound[0]:
            return True

    return False


def hasCycleHelper(graph, node, cycleFound, prevNode, marked):
    if cycleFound[0]:
        return
    marked[node] = True
    for node2 in graph.adj[node]:
        if marked[node2] and node2 != prevNode:
            cycleFound[0] = True
            return
        if marked[node2] == False:
            hasCycleHelper(graph, node2, cycleFound, node, marked)


def is_connected(graph):
    for i in graph.adj:
        for j in graph.adj:
            if BFS2(graph, i, j) == []:
                return False
    return True


A = Graph(10)
for i in range(0, 9):
    A.add_edge(i, i+1)

# A.add_edge(9, 1)

# G = Graph(11)
# G.add_edge(1, 5)
# G.add_edge(3, 7)
# G.add_edge(2, 1)
# G.add_edge(3, 9)
# G.add_edge(8, 4)
# G.add_edge(6, 10)
# G.add_edge(10, 2)
# G.add_edge(8, 9)
# G.add_edge(7, 5)
# G.add_edge(9, 7)
# G.add_edge(1, 4)
# G.add_edge(5, 9)
# G.add_edge(7, 4)
# G.add_edge(1, 10)
# G.add_edge(10, 3)
# G.add_edge(4, 3)


# H = Graph(6)
# H.add_edge(0, 2)
# H.add_edge(2, 5)
# H.add_edge(1, 0)
# H.add_edge(1, 3)
# H.add_edge(1, 4)
# H.add_edge(4, 5)


# X = Graph(7)
# X.add_edge(1, 2)
# X.add_edge(1, 3)
# X.add_edge(2, 4)
# X.add_edge(3, 4)
# X.add_edge(3, 5)
# X.add_edge(4, 5)
# X.add_edge(4, 6)


# print(BFS2(G, 8, 1))
# print(DFS2(G, 8, 1))
# print(DFS(G, 8, 1))

# print(DFS(H, 0, 5))
# print(DFS2(H, 0, 5))
# print(BFS2(H, 0, 5))
# print(DFS2(A, 0, 9))
# print(BFS2(A, 0, 9))

# print(has_cycle(X))
# print(has_cycle(G))
# print(has_cycle(A))


# print(is_connected(G))
# print(is_connected(X))
# print(is_connected(H))
# print(is_connected(A))
