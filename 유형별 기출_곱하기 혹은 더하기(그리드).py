s = str(input())

#결과를 담을 변수
result = int(s[0])


#두번째 문자부터 하나씩 꺼내서 더하거나 곱할건데
for i in s[1:]:
    #꺼낸 값이 0이거나 현재 결과값이 0이면
    if int(i)==0 or result==0:
        result +=int(i)
    else:
        result *=int(i)
print(result)

