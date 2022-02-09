P = int(input())
n = int(input())
R = int(input())

total = n
days = 0
while total <= P:
    n *= R
    total += n

    days += 1

print(days)