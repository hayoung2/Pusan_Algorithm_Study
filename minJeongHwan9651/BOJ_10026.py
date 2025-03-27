import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs_blue(y: int, x: int):
    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if visited[ny][nx] == 1:
            continue

        if color_list[ny][nx] == 'R':
            continue
        if color_list[ny][nx] == 'G':
            continue

        dfs_blue(ny, nx)

def dfs_red(y: int, x: int):
    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if visited[ny][nx] == 1:
            continue

        if color_list[ny][nx] == 'B':
            continue
        if color_list[ny][nx] == 'G':
            continue

        dfs_red(ny, nx)

def dfs_green(y: int, x: int):
    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if visited[ny][nx] == 1:
            continue

        if color_list[ny][nx] == 'R':
            continue
        if color_list[ny][nx] == 'B':
            continue

        dfs_green(ny, nx)

def dfs_green_red(y: int, x: int):
    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if visited[ny][nx] == 1:
            continue

        if color_list[ny][nx] == 'B':
            continue

        dfs_green_red(ny, nx)

###########################

N = int(input())

color_list = []
cnt_blue = 0
cnt_red = 0
cnt_green = 0
cnt_green_red = 0

for i in range(N):
    color_list.append(input())


visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            continue
        if color_list[i][j] == 'R':
            continue
        if color_list[i][j] == 'G':
            continue

        cnt_blue += 1
        dfs_blue(i, j)

visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            continue
        if color_list[i][j] == 'B':
            continue
        if color_list[i][j] == 'G':
            continue

        cnt_red += 1
        dfs_red(i, j)

visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            continue
        if color_list[i][j] == 'R':
            continue
        if color_list[i][j] == 'B':
            continue

        cnt_green += 1
        dfs_green(i, j)

visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            continue
        if color_list[i][j] == 'B':
            continue

        cnt_green_red += 1
        dfs_green_red(i, j)


print(cnt_blue + cnt_green + cnt_red, end=' ')
print(cnt_blue + cnt_green_red)