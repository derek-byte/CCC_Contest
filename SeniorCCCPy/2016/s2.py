q = int(input())
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

ans = 0
if q == 1:
  x.sort()
  y.sort()
  
else:
  x.sort()
  y.sort(reverse=True)

for i in range(n):
    ans += max(x[i], y[i])

print(ans)