while True:
    hour, minute = map(int, input().split())
    if 0 <= hour <= 23 and 0 <= minute <= 59:
        break

Hadd = hour
Madd = minute - 45

if Madd < 0:
    Hadd -= 1
    Madd += 60
    if Hadd < 0:
        Hadd = 23

print(Hadd, Madd)
