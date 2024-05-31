import sys
import heapq as hq
input = sys.stdin.readline

V,E = map(int,input().split(' '))
K = int(input())

graph = [[] for _ in range(V+1)] # 0번째는 사용 X

for _ in range(E):
  u,v,w = map(int,input().split(' '))
  graph[u].append((w,v))

distances = [float('inf')]*(V+1)
distances[K] = 0
pq = [(0,K)]
while pq:
  distance, vertex = hq.heappop(pq)

  if distance > distances[vertex]:
    continue

  for weight, neighbor in graph[vertex]:
    new_distance = distance + weight

    if new_distance < distances[neighbor]:
      distances[neighbor] = new_distance
      hq.heappush(pq, (new_distance, neighbor))

for i in range(1,V+1):
  if distances[i] == float('inf'):
    print("INF")
  else:
    print(distances[i])