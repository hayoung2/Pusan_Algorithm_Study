import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

x = 0
t = 0

find_list = deque()

visited = [0 for _ in range(100001)]


find_list.append(N)

while find_list:
    for _ in range(len(find_list)):
        x = find_list.popleft()

        if x == K:
            print(t)
            exit(0)

        for i in (x - 1, x + 1, x * 2):
            if i < 0 or i > 100000:
                continue
            if visited[i] == 1:
                continue

            visited[i] = 1
            find_list.append(i)
    t += 1
