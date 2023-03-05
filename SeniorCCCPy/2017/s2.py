n = int(input())

x = list(map(int, input().split()))

x.sort(reverse=True)
high = x[:len(x)//2][::-1]
low = x[len(x)//2:]
# print(x, low, high)

ans = ""
for i in range(len(high)):
  ans += str(low[i]) + " " + str(high[i]) + " "

if len(low) > len(high):
  ans += str(low[-1])
else:
  ans = ans[:-1]

print(ans)