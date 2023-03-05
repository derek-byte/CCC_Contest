n = int(input())

c = []
for i in range(3):
  c.append(int(input()))

x = ""
while x != 77:
  x = int(input())

  if x == 99:
    river = int(input()) - 1
    percent = int(input()) / 100
    c[river] = int(c[river]*percent)
    c.insert(river, c[river])
  elif x == 88:
    river = int(input()) 
    c[river-1] += c[river]
    c.pop(river)

ans = ""
for i in range(len(c)):
  ans += str(c[i]) + " "

print(ans)