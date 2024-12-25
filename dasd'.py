n = int(input())

data = []

for _ in range(10):
    data.append(int(input()))

print(data)

result =[[] for _ in range(10)]

print(result)

for i in range(10):
    for j in range(0,i):
        sum += data[j]
