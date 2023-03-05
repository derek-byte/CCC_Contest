n = int(input())

arr = []
for i in range(n):
  arr.append(int(input()))
arr.sort()

areas = []
for i in range(n-1):
  areas.append((arr[i+1] - arr[i]) / 2)

ans = 1000000000000
for i in range(1, len(areas)):
  if areas[i] + areas[i-1] < ans:
    ans = areas[i] + areas[i-1]

print(ans)