n = int(input())

array = list(map(int, input().split()))

d = [0] *100

d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+ array[i])

print(d[n-1])


##(i-1)번째 식량창고를 털기로 결정한 경우 현재의 식량 창고를 털 수 없다.
##(i-2)번째 식량창고를 털기로 결정한 경우는 현재의 식량 창고를 털 수 있다.
##따라서 i번째의 식량 창고에 대한 최적의 해는 d[i] = max(d[i-1], d[i-2]+ array[i])이다