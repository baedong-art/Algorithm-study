#내 답안
s = input()

alpa = []
isalpa = []
num = 0
#리스트에 값넣기 ###굳이 리스트에 한번더 넣지 안혹 바로 꺼내서 쓰는 편이 더 효율적이다
for i in s:
    alpa.append(i)


#리스트를 확인하면서 알파벳은 숫자형태로 변경
for i in alpa:
    #알파벳이면 알파벳 리스트에 넣기
    if i.isalpha() == True:
        isalpa.append(i)
    #숫자면 합산
    else:
        num +=int(i)

#오름차순으로 정렬
isalpa.sort()

# 숫자를 문자열로 변환하여 이어 붙이기 리스트에 있는값 띄어쓰기 없이 붙이는 join 기억하기
#####이렇게 하는경우 입력받은 문자열안에 숫자가 없는경우 예외처리가 안됌
result = ''.join(isalpa) + str(num)

print(result)

#답안지

data = input()
result = []
value = 0

#문자를 하나씩 확인하며
for x in data:
    #알파벳인 경우 결과리스트에 삽입
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value !=0:
    result.append(str(value))

print(''.join(result))