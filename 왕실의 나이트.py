#현재 나이트의 위치 입력받기

dic  = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
input_data = input()
row = int(input_data[1])
column = dic.get(input_data[0])

#
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인

result = 0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column +step[1]
    if next_row  >=1 and next_row <=8 and next_column>=1 and next_column <=8:
        result +=1
print(result)