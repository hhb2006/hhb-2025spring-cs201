class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def main():
    graph = Graph()
    n, m = map(int, input().split())

    for i in range(n):
        graph.addVertex(i)

    for _ in range(m):
        a, b = map(int, input().split())
        graph.addEdge(a, b)
        graph.addEdge(b, a)

    laplacianMatrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                laplacianMatrix[i][j] = len(graph.vertList[i].connectedTo)
            else:
                v1, v2 = graph.vertList[i], graph.vertList[j]
                if v2 in v1.connectedTo:
                    laplacianMatrix[i][j] -= 1
        print(*laplacianMatrix[i])


if __name__ == '__main__':
    main()