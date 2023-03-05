n = input()

arr = [[1, 2], [3, 4]]

for i in n:
  if i == "H":
    arr[0][1], arr[0][0] = arr[0][0], arr[0][1]
    arr[1][1], arr[1][0] = arr[1][0], arr[1][1]
  else: 
    arr[0], arr[1] = arr[1], arr[0]

print("{} {} \n{} {}".format(arr[0][0], arr[0][1], arr[1][0], arr[1][1]))