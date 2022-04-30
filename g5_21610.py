# 바구니 (r,c) 단, (1,1) ~ (N,N)
# A[r][c]:물양
# 첫번째 구름 (N,1) (N,2) (N-1,1), (N-1,2)
import sys
#sys.setrecursionlimit = 10**6

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dir = [0 for _ in range(M)]  # 방향
move = [0 for _ in range(M)]  # 몇 걸음
info = []
for i in range(M):
    info = list(map(int, sys.stdin.readline().split()))
    dir[i] = info[0]
    move[i] = info[1]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 이동 function (제일 끝 연결됨)


def moving(iter, start_x, start_y):
    global visited
    nx = start_x + (dx[dir[iter]-1] * move[iter])  # dir 바꿔줘야함!!!
    ny = start_y + (dy[dir[iter]-1] * move[iter])
    if nx >= 0:
        new_nx = abs(nx) % N
    else:
        if N - abs(nx) % N != N:
            new_nx = N-abs(nx) % N
        else:
            new_nx = 0

    if ny >= 0:
        new_ny = abs(ny) % N
    else:
        if N - abs(ny) % N != N:
            new_ny = N-abs(ny) % N
        else:
            new_ny = 0

    moved.append([new_nx, new_ny])
    visited[new_nx][new_ny] = True
    A[new_nx][new_ny] += 1
    # print(moved)
    # print(A)


tx = [-1, -1, 1, 1]  # 상상하하
ty = [-1, 1, 1, -1]  # 좌우우좌
# 비복사 function (제일 끝 끊김)


def rain(rain_x, rain_y):
    cnt = 0
    for i in range(4):
        nx = rain_x + tx[i]
        ny = rain_y + ty[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        elif A[nx][ny] > 0:
            cnt += 1
    # print(cnt)
    A[rain_x][rain_y] += cnt
    # print(A)

# 구름 function (마지막으로 구름이 있었던 곳을 제외하고, 물의 양이 2이상인 곳 구름)
# def cloud(rain_x, rain_y):
#     start = []
#     for i in range(N):
#         for j in range(N):
#             if i == rain_x and j == rain_y : continue
#             elif A[i][j] >= 2:
#                 A[i][j] -= 2
#                 start.append([i,j])
#     print(A)


def cloud(moved, visited):
    global next_start
    next_start = []
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and visited[i][j] == False:
                A[i][j] -= 2
                next_start.append([i, j])  # 다음 input으로
    # print(next_start)
    # print(A)


# 식 세우기
start = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
iter = 0
for it in range(M):  # 4번 이동, it = 0,1,2,3
    moved = []  # 이동된 구름 저장, 단 매번 초기화해야함
    # print(moved)
    if it == 0:
        next_start = start

    visited = [[False]*N for _ in range(N)]
    for i in next_start:
        moving(iter, i[0], i[1])  # 구름 이동
    # start = [] #start초기화
    for j in moved:
        rain(j[0], j[1])  # moving의 return값을 rain에 넣어줌

    cloud(moved, visited)  # 이 cloud가 다음 구름 input이 된다
    iter += 1

# 모든 이동이 끝나고 난 후, 물의 양의 합
water = 0
for i in range(N):
    for j in range(N):
        water += A[i][j]
print(water)