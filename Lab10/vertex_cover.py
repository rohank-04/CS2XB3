import random


class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def hasEdge(self, node1, node2):
        return node2 in self.adj[node1]

    def addEdge(self, node1, node2):
        if not self.hasEdge(node1, node2):
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def removeEdge(self, node1, node2):
        if self.hasEdge(node1, node2):
            self.adj[node1].remove(node2)
            self.adj[node2].remove(node1)

    def getSize(self):
        return len(self.adj)


def untrackedEdge(vc, G):

    for i in G.adj.keys():
        for j in G.adj[i]:
            if i not in vc and j not in vc:
                return (i, j)

    return None


def nodeWithMaxEdges(G, edge):
    length0 = len(G.adj[edge[0]])
    length1 = len(G.adj[edge[1]])

    if length0 >= length1:
        return edge[0]
    else:
        return edge[1]


def vertex_cover1(G):
    # Initialize vc to []
    vc = []

    # Get edge that is not in vc yet
    x = untrackedEdge(vc, G)

    while x != None:

        vc.append(nodeWithMaxEdges(G, x))

        x = untrackedEdge(vc, G)

    return vc


def vertex_cover2(G):
    # Initialize vc to []
    vc = [a for a in G.adj.keys()]

    gCopy = G

    for i in gCopy.adj.keys():
        if nodeReplaceable(gCopy, i):
            print(i)
            replaceNode(gCopy, i)
            vc.remove(i)

    return vc


def nodeReplaceable(G, node):

    for i in G.adj[node]:
        if i == -1:
            return False
    return True


def replaceNode(G, node):
    for i in G.adj.keys():
        G.adj[i] = [-1 if x == node else x for x in G.adj[i]]

    return G.adj




# G = Graph(6)
# G.addEdge(0, 1)
# G.addEdge(1, 2)
# G.addEdge(1, 3)
# G.addEdge(2, 4)
# G.addEdge(4, 3)
# G.addEdge(2, 5)

# G0 = Graph(9)
# G0.addEdge(0,1)
# G0.addEdge(1,2)
# G0.addEdge(3,4)
# G0.addEdge(4,5)
# G0.addEdge(6,7)
# G0.addEdge(7,8)
# G0.addEdge(0,3)
# G0.addEdge(3,6)
# G0.addEdge(1,4)
# G0.addEdge(4,7)
# G0.addEdge(2,5)
# G0.addEdge(5,8)

# G1 = Graph(6)
# G1.addEdge(0,1)
# G1.addEdge(0,3)
# G1.addEdge(0,5)
# G1.addEdge(1,2)
# G1.addEdge(1,4)
# G1.addEdge(2,3)
# G1.addEdge(2,5)
# G1.addEdge(3,4)
# G1.addEdge(4,5)

# G2 = Graph(9)
# G2.addEdge(3, 5)
# G2.addEdge(5, 6)
# G2.addEdge(1, 2)
# G2.addEdge(1, 4)
# G2.addEdge(4, 3)
# G2.addEdge(5, 7)
# G2.addEdge(2, 8)
# G2.addEdge(2, 3)

# print(untrackedEdge([2, 4, 5], G2))
print(vertex_cover2(G1))
