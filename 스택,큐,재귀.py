from collections import deque
####스택
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #최하단 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력

#### 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

#재귀함수
def recursive_function():
    print("재귀 함수를 호출합니다.")
    recursive_function()
recursive_function()

def factorial_iterative(n):
    result = 1
    #1부터 n까지의 수를 차례대로 곱하기
    for i in range(1,n+1):
        result *=i
    return result


# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n<=1:
        return 1
    return n *factorial_iterative(n-1)


