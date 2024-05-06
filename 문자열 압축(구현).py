import re
def solution(s):
    if len(s) <=2:
        return len(s)
    resultCount = []
    for i in range(1, len(s)//2 + 1):
        reList = re.sub('(\w{%i})'   %i, '\g<1> ',s).split()
        count = 1
        result  = []
        for j in range(len(reList)):
            #범위에서 벗어나지 않고 현재 문자와 다음 문자가 같다면 count + 1
            if j <len(reList)-1 and reList[j] == reList[j+1]:
                count +=1
            #문자가 다를 경우
            else:
                #count가 1이면 그대로 result에 넣고
                if count == 1:
                    result.append(reList[j])
                #2이상이면 붙여서 넣는다
                else:
                    result.append(str(count)+ reList[j])
                    count = 1
        resultCount.append(len(''.join(result)))
    return min(resultCount)
