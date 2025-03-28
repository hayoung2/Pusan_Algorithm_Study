import sys
from collections import deque

visit_list = deque()
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


input = sys.stdin.readline

M, N = map(int, input().split())

visited = [[0 for _ in range(M)] for _ in range(N)]

tomato_arr = []
cnt = -1
flag = 0

for i in range(N):
    tomato_arr.append(list(map(int, input().split())))


for i in range(N):
    for j in range(M):
        if tomato_arr[i][j] == 1:
            visit_list.append((i, j))

while visit_list:
    for _ in range(len(visit_list)):
        (y, x) = visit_list.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if tomato_arr[ny][nx] == 1 or tomato_arr[ny][nx] == -1:
                continue
            if visited[ny][nx] == 1:
                continue

            visited[ny][nx] = 1
            tomato_arr[ny][nx] = 1
            visit_list.append((ny, nx))
    cnt += 1
    

for i in range(N):
    for j in range(M):
        if tomato_arr[i][j] == 0:
            flag = 1

if flag == 1:
    print(-1)
else:
    print(cnt)
