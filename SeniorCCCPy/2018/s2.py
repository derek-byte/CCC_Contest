n = int(input())

arr = []
for i in range(n):
  x = list(map(int, input().split()))
  arr.append(x)

c1 = arr[0][0]
c2 = arr[0][n-1]
c3 = arr[n-1][0]
c4 = arr[n-1][n-1]

m = min([c1, c2, c3, c4])

ans = []
if m == c2:
  for i in range(len(arr)):
    t = []
    for j in range(len(arr)):
      t.append(arr[j][i])
    ans.append(t)
  ans = ans[::-1]

elif m == c3:
  for i in range(len(arr)):
    t = []
    for j in range(len(arr)):
      t.append(arr[j][i])
    ans.append(t[::-1])

elif m == c4:
  for i in range(len(arr)):
    arr[i] = arr[i][::-1]   
  ans = arr[::-1]
  
else:
  ans = arr

for i in range(len(ans)):
  s = ' '.join(map(str,ans[i]))
  print(s)