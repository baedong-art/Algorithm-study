n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    #이름은 문자열 그래도, 정수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))


#키를 이용하여, 정수를 기준으로 정렬 student라는 것으로 칭한다
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end= ' ')
