n = int(input())

n1 = input()
h = []
num = ""
for i in range(len(n1)):
  if n1[i] == " ":
    h.append(int(num))
    num = ""
  else:
    num += n1[i]
h.append(int(n1[-1]))

n2 = input()
w = []
num = ""
for j in range(len(n2)):
  if n2[j] == " ":
    w.append(int(num))
    num = ""
  else:
    num += n2[j]
w.append(int(n2[-1]))

# print(h, w)

t_area = 0
for i in range(n):
  area = (w[i] * (h[i] + h[i+1])) / 2
  t_area += area
  # print(area)

print(t_area)

# num =int(input())
# l1 = list(map(int, input().split()))
# l2 = list(map(int, input().split()))
# t = 0

# for i in range(num):
#     t += ((l1[i] + l1[i + 1]) * l2[i]) / 2

# print(t)