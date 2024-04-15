#피보나치 함수(Fibonacci Function)를 재귀 함수로 구현
# def fibo(x):
#     if x== 1 or x==2:
#         return 1
#     return fibo(x-1) + fibo(x-2)
# print(fibo(4))


#####피보나치 수열 소스코드(재귀적)
# d = [0] * 100
#
# #피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그램)
# def fibo(x):
#     if x ==1 or x ==2:
#         return 1
#     #이미 계산한 적이 있는 문제라면 그대로 반환
#     if d[x] !=0:
#         return d[x]
#     #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
#     d[x] = fibo(x-1) +fibo(x-2)
#     return d[x]
#
# print(fibo(99))


#호출 되는 함수 확인
d =[0] * 100

def pibo(x):
    print('f('+str(x)+')', end=' ')
    if x==1 or x==2:
        return 1
    if d[x] !=0:
        return d[x]
    d[x] = pibo(x-1)+ pibo(x-2)
    return d[x]
pibo(6)

#피보나치 수열 소스코드(반복적)
d =[0] * 100

d[1] = 1
d[2] = 1
n = 99

#피보나치 함수 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3,n+1):
    d[i] = d[i-1]+ d[i-2]

print(d[n])