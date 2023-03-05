x = sorted(input())
n = input()
arr = []

ans = 0
for i in range(len(x), len(n)+1):
  y = sorted(n[i-len(x): i])
  # print(y, arr)
  if x == y and n[i-len(x):i] not in arr:
    ans += 1
    arr.append(n[i-len(x):i])

print(ans)