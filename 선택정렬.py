array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

#가장 작은 원소를 맨앞으로 보내는 과정을 n-1번 반복
for i in range(len(array)):
    #처음 숫자를 최소값으로 지정
    min_index = i
    #가장 작은 원소를 맨앞으로 보낸다
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    #두 원소 스왑
    array[i], array[min_index] =array[min_index], array[i]

print(array)