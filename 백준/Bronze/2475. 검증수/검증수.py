numbers = list(map(int, input().split()))

number = sum(num ** 2 for num in numbers) % 10

print(number)
