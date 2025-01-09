N = int(input())

numbers = []
for num in range (N):
    numbers.append(int(input()))

numbers.sort()

for num in numbers:
    print(num)