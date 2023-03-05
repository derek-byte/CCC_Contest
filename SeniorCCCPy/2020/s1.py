n = int(input())

arr = []
for i in range(n):
  x = list(map(int, input().split()))
  arr.append(x)

arr.sort(key=lambda x:x[0])

ans = 0
for i in range(1, len(arr)):
  speed = abs((arr[i][1] - arr[i-1][1]) / (arr[i][0] - arr[i-1][0]))

  if speed > ans:
    ans = speed

print(ans)