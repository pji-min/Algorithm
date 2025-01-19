n, b = map(int, input().split())
d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = []
while n > 0:
    result.append(d[n % b])
    n //= b
print(''.join(result[::-1]))