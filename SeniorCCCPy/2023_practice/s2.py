n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

x_sum = 0
y_sum = 0
ans = 0
for i in range(n):
  x_sum += x[i]
  y_sum += y[i]
  # print("SUM",x_sum, y_sum)
  if x_sum == y_sum:
    # print(x[i], y[i], i)
    ans = i+1

print(ans)