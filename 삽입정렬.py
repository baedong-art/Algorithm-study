array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

#두번째 인덱스부터 앞 인덱스 비교
for i in range(1,len(array)):
    #i번째 부터 첫번째 인덱스까지 1씩 감소시키면서 비교
    for j in range(i, 0, -1):
        if array[j] < array[j-1]: #한칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춘다.
            break
print(array)

