while True:
    hour, minute = map(int, input().split())
    if 0 <= hour <= 23 and 0 <= minute <= 59:
        break

while True:
    time = int(input())
    if 0 <= time <= 1000:
        break

Hadd = 0
Madd = minute + time

while Madd >= 60:
    Madd -= 60
    Hadd += 1

Hadd += hour
Hadd %= 24

print(Hadd, Madd)
