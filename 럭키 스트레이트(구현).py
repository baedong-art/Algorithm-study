
#내가 푼 정답
n = int(input())

m = str(n)
lengh = len(m)

left = 0
right = 0

#left 넣기
for i in m[:lengh//2]:
    left += int(i)

for i in m[lengh//2:]:
    right += int(i)

print(left, right)

if left ==right:

    print("LUCKY")
else:
    print("READY")


#####답안지

n = input()
length = len(n) #점수값의 총 자릿수
summary = 0

#왼쪽 부분의 자릿수 합 더하기
for i in range(length//2):
    summary += int(n[i])

#오른쪽 부분의 자릿수 합 빼기
for i in range(length//2, length):
    summary -= int(n[i])

#왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary ==0:
    print("LUCKY")
else:
    print("READY")