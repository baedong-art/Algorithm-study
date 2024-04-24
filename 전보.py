import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

#노드 개수, 간선 개수, 시작 노드를 입력받기
n, m, start =map(int, input().split())


graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

#모든 간선 정보 입력받기
for _ in range(m):
    x,y,z = map(int, input().splti())
    graph[x].append((y,z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        #가장 최단거리의 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 길이가 꺼낸 노드보다 작다면  그냥 무시
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #만약 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost <distance[i[0]]:
                distance[i[0]] =  cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

count  = 0

max_distance = 0
for d in distance:
    if d !=INF:
        count +=1
        max_distance = max(max_distance,d)

#시작 노드는 제죄해야 하므로  count -1 출력
print(count-1, max_distance)