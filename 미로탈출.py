from collections import deque

n, m  = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))


#이동할 네 방향 정의(상,하,좌,우)
dx = [-1,1,0,0,]
dy = [0,0,-1,1]

#BFS 소스 구현

def bfs(x,y):

    queue = deque()
    queue.append((x,y))

    #큐가 빌 때까지 반복
    while queue:
        x,y =queue.popleft()
        #현재 위치에서 네방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 공간을 벗어난 경우 무시
            if nx <0 or ny <0 or nx >=n or ny>=m:
                continue
            #벽인 경우는 무시
            if graph[nx][ny] ==0:
                continue
            #길인 경우 1을 더해 거리를 추가해주고 다음 노드를 큐에 넣어준다
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y] + 1
                graph.append((nx,ny))
    #오른쪽 맨 아래까지의 최단거리 변환
    return graph[n-1][m-1]

#시작점부터  bfs 시작
print(bfs(0,0))