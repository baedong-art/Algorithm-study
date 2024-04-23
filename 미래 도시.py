INF = int(1e9)

n,m =map(int, input().split())
gragh = [[INF] *(n+1) for _ in range(1, n+1)]


#자기 자신에서 자신으로 가는 비용은 0으로초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            gragh[a][b] = 0

#각 간선에 대한 정보를 입력받아 , 그값으로 초기화
for _ in range(m):
    a,b = map(int, input().split())
    gragh[a][b] =1
    gragh[b][a] =1

#거쳐 갈 노드 x와 최종 목적지 노드 K를 입력받기
x,k =map(int, input().split())

for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            gragh[a][b] = min(gragh[a][b], gragh[a][k]+gragh[k][b])

#수행된 결과를 출력
distance = gragh[1][k]+gragh[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)