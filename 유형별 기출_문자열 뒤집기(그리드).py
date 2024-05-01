s =  str(input())

#연속된 0과 1의 변수
count0 = 0
count1 = 0

if s[0] == '0':
    count0 +=1
else:
    count1 +=1


#두 번째 원소부터 모드 원소를 확인하며
for i in range(1,len(s)):
    if s[i-1] != s[i]: #이전값
        if s[i] =='1': #다음수에서 1로 바뀌는 경우
            count0 +=1
        else:
            count1 +=1
print(min(count1,count0))
