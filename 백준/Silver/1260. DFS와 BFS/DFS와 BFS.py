import sys
from collections import defaultdict,deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

[N,M,V] = map(int,input().split(' '))

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)
    self.visited = [False for _ in range(N+1)]    

  def add_edge(self,u,v):
    self.graph[u].append(v)
    self.graph[v].append(u)

  def print_graph(self):
    for node in self.graph:
      print('key',node,':',self.graph[node])

  def dfs(self,v):
    if self.visited[v]:
      return
    else:
      self.visited[v]=True
      print(v, end=" ")
      for u in sorted(self.graph[v]):
        self.dfs(u)

  def bfs(self,start):
    q = deque([])
    q.append(start)
    while q:
      v = q.popleft()
      if not self.visited[v]:
        print(v, end=" ")
        self.visited[v]=True
        for u in sorted(self.graph[v]):
          if not self.visited[u]:
            q.append(u)

  def visited_intialize(self):
    self.visited = [False for _ in range(N+1)] 

al=Graph()
for _ in range(M):
  [u,v] = map(int,input().split(' '))
  al.add_edge(u,v)

al.dfs(V)
al.visited_intialize()
print()
al.bfs(V)