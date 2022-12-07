from collections import defaultdict
class Graph:
    def _init_(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v,end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)
g = Graph()
n=int(input("Enter number of edges : "))
for i in range(n):
  x,y=map(int,input("Enter source and destination : ").split()[:2])
  g.addEdge(x,y)
source = int(input("Enter source node : "))
g.DFS(2)
