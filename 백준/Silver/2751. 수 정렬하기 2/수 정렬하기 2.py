import sys

input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
numbers = [int(input()) for _ in range(N)]

numbers.sort()

output("\n".join(map(str, numbers)) + "\n")
