rows = int(input())
columns = int(input())

# arr = [["B"]*columns]*rows
arr = []
for i in range(rows):
  a = []
  for j in range(columns):
    a.append(0)
  arr.append(a)

ans = 0
n = int(input())
for i in range(n):
  option = input()
  option = option.split(" ")
  val = int(option[1])-1

  if option[0] == "R":
    for j in range(len(arr[val])):
      if arr[val][j] == "B":
        arr[val][j] += 1
        ans += 1
      else:
        arr[val][j] = "B"
        ans -= 1
  else: 
    for j in range(len(arr)):
      if arr[j][val] == "B":
        arr[j][val] += 1
        ans += 1
      else:
        arr[j][val] = "B"
        ans -= 1

  # print(arr)

# for i in range(len(arr)):
#   if arr[i]
print(ans)