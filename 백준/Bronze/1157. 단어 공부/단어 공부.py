from collections import Counter

word = input().strip().upper()

counter = Counter(word)

maxCount = max(counter.values())
add = [key for key, value in counter.items() if value == maxCount]

if len(add) > 1 :
    print("?")
else:
    print(add[0])
