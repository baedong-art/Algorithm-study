##신장 트리란 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의마한다.
#크루스칼 알고리즘은 최소한의 비용으로 신장트리를 찾아야 할 때 사용하는 알고리즘이다.
def find_parent(parent, x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0] *(v+1)

####모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

#부모테이블 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a,b, cost = map(int, input().split())
    edges.append((cost,a,b))

#정렬 cost가 첫번째 원소이기 때문에 cost순으로 나열된다
edges.sort()

#간선을 하나씩 확인
for edge in edges:
    cost, a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)
