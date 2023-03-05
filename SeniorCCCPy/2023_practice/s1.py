n = int(input())

arr = []
ans = 0
for i in range(1, n):
  for j in range(1, n):
    if i + j == n and (i not in arr or j not in arr) and i<6 and j<6 and i >= j:
      arr.append(i)
      arr.append(j)
      ans += 1
      # print(i, j)

if n > 5:
  print(ans)
else:
  print(ans+1)