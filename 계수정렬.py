array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 모든 번위를 포함하는 리스트 선언(모든값은 0으로 초기화)
count = [0] *(max(array)+1)

for i in range(len(array)):
    count[array[i]] +=1 #각 데이텅에 해당한느 인덱스의 값증가

print(count )
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')