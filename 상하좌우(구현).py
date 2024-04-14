n = int(input())
plans = input().split()

x,y =1,1 #시작지점 설정

#L,R,U,D
dx = [0,0,-1,1]
dy = [-1,1,0,0]

move_types = ['L','R','U','D']

for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan ==move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #이동 후 공간을 벗어나느 경우 무시
    if nx < 1 or ny < 1 or nx >n or ny > n:
        continue
    #벗어나지 않는다면 좌표값 갱신
    x, y = nx, ny

print(x,y)