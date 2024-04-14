n = int(input())

array =[]

for i in range(n):
    array.append(int(input()))

#파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
array = sorted(array, reverse=True)

#수행결과 출력
for i in array:
    print(i, end=' ')