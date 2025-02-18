import sys
from collections import defaultdict

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
check_cards = list(map(int, input().split()))

count = defaultdict(int)
for card in cards:
    count[card] += 1

for card in check_cards:
    print(count[card], end=' ')
