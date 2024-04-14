n, k  = map(int, input().split())

result = 0
while n >=k:# n이 나누는 수 이상이면 계속 나눈다
    while n%k !=0: #근데 나누어지지 않으면 1을 빼고 횟수 1증가
        n  -=1
        result +=1
    n //=k #나누어지면 나누고 횟수증가
    result +=1
while n >1: #이제 나누려고 하는 숫자보다 작기때문에 1씩 빼주면서 횟수를 증가시켜야 한다.
    n -=1
    result +=1
print(result)
