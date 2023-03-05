n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

ans = 0
s1 = 0
s2 = 0
for i in range(len(x)):
  s1 += x[i]
  s2 += y[i]

  if s1 == s2:
    ans = i + 1

print(ans)