import sys
from collections import defaultdict

N = int(input())
cards = [int(input()) for _ in range(N)]

count = defaultdict(int)
for card in cards:
    count[card] += 1
    
max_count = 0
result = 0
for card, f in count.items():
    if f > max_count:
        max_count = f
        result = card
    elif f == max_count and card < result:
        result = card

print(result)
