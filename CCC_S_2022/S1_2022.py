N = int(input())

counter = 0

for x in range(N):
    y = ((N-(4*x))//5)
    ans = (4*x) + (5*y)
    if ans == N and (4*x) >= 0 and (5*y) >= 0:
        counter += 1 

print(counter)