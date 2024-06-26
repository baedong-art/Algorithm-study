n,m = map(int, input().split())

# direction 0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽
x,y,direction = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
d[x][y] = 1 #현재위치 방문 처리
#맵 전체 정보 입력 받기
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

#북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


#시뮬레이터 시작
count =1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x +dx[direction]
    ny = y +dy[direction]
    #회전한 이후 정면에 가보지 않은 곳(d)이며 육지이면(array) 방문처리 후 위치 갱신
    if d[nx][ny] == 0 and array[nx][ny] ==0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        #다시 회전 횟수 초기화
        turn_time =0
        continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time +=1
    if turn_time ==4:
        nx = x -dx[direction]
        ny = y -dy[direction]
        #뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀잇는 경우
        else:
            break
        turn_time = 0

print(count)