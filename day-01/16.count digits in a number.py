#16. Count digits in a number
n = 12345

count = 0

while n > 0:
    count += 1
    n //= 10

print(count)