#2차원 리스트 90도 회정
def rotate_a_matrix_by_90_degree(a):
    n = len(a) #행 길이 계산
    m = len(a[0])#열 길이 계산

    result = [[0] * n for _ in range(m)] #결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

# 자물쇠 중간 부분이 모두 1인지 확인
def check(new_lock):
    # 3배 이상 늘려서 계산했기 때문에 줄여준다
    lock_length = len(new_lock) // 3
    for i in range(lock_length,lock_length *2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] !=1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    #자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    #새로운 자물쇠의 중앙 부분에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    #4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) #열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                #자물쇠에 열쇠를 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                #새로운 자물쇠에 열쇠가 정확히 들어맞는 지 검사
                if check(new_lock)  == True:
                    return  True
                #자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False


##########다른 풀이

def match(arr, key,rot, r,c):
    n = len(key)
    #열쇠 복사
    for i in range(n):
        for j in range(n):
            if rot == 0:
                #1인지를 확인해야 하기때문에 +=
                arr[r+i][c+j] += key[i][j]
            elif rot ==1: #90도
                arr[r+i][c+j] +=key[n-1-j][i]
            elif rot ==2: #180도
                arr[r+i][c+j] += key[n-1-j][n-1-j]
            else: #270도
                arr[r + i][c + j] += key[j][n-1-i]

def check(arr, offset,n):
    for i in range(n):
        for j in range(n):
            if arr[offset + i][offset + j] !=1:
                return False
    return True

def solution(key, lock):
    offset = len(key) - 1

    #행
    for r in range(offset + len(lock)):
        #열
        for c in range(offset + len(lock)):
            #회전
            for rot in range(4):
                arr = [[0 for _ in range(58)] for _ in range(58)]
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        #가운데 자물쇠 복사
                        arr[offset + i][offset +j] = lock[i][j]
                match(arr, key, rot, r,c)
                if check(arr, offset, len(lock)):
                    return  True
    return False