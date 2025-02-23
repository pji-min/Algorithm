import sys

N = int(sys.stdin.readline().strip())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

points.sort()

for x, y in points:
    print(x, y)
