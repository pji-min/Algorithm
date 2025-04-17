import math

def count(N, M):
    return math.comb(M, N)

t = int(input())

for _ in range(t):
    N, M = map(int, input().split())
    print(count(N, M))
