#위상 정렬이란 순서가 정해져있는 일련의 작업을 차례대로 수행해야 할때 사용하는 알고리즘
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

##진입 차수 : 특정한 노드로 들어오는 간선의 개수를 의미

from collections import deque

#노드와 간선의 개수를 입력받는다
v,e = map(int, input().split())

#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] *(v+1)
#각 노드에 연결된 간선 정보를 담기위한 연결리스트(그래프) 초기화
graph = [[] for _ in range(v+1)]

#방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b) #정점 A에서B로 이동가능
    #진입차수 1 증가
    indegree[b] +=1

print(graph)
print(indegree)

#위상 정렬 함수
def topology_sort():
    result = [] #결과를 담을 리스트 선언
    q = deque()

    #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    #큐가 빌때까지 반복
    while q:
        now = q.popleft()
        #결과값에 추가
        result.append(now)
        print(graph[now])
        #해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            print(i)
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()