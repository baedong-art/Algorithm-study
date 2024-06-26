n,k = map(int, input().split())

thing = [[0,0]]

d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))
# print(thing)

for i in range(1,n+1):
    for j in range(1,k+1):
        w = thing[i][0]
        v = thing[i][1]

        #현재 배낭의 허용 무게보다 넣을 무건의 무게가 더 크다면 넣지않는다
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j]  = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])