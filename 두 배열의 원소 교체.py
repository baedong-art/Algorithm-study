n, m =map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()#오름차순으로 정렬
b.sort(reverse=True)# 내림차순으로  정렬

for i in range(m):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: #a의 원소가 b원소보다 크거나 같을 때 반복문을 탈출
        break
print(sum(a))
