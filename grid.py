n ,m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1] #가장 높은 수
second = data[-2] #두번째로 높은수

result = 0

while True:
    for i in range(k): #가장 큰수 3번 더하기
        if m == 0: #m이 0이라면 반복문 탈출
            break
        result += first
        m -=1
    if m == 0: #m이 0이라면 반복문 탈출
        break
    result += second
    m -=1

print(result)