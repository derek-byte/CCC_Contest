n = int(input())
arr = []
vals = {}

for i in range(n):
  x = int(input())
  arr.append(x)
  if x in vals:
    vals[x] += 1
  else:
    vals[x] = 1
    
arr.sort()
arr = arr[::-1]

minimum_num = 1000000000000000000000000000
min_q = 0
for i, v in vals.items():
  if v > min_q:
    minimum_num = i
    min_q = v
  elif v == min_q and minimum_num > i:
    minimum_num = i
    min_q = v
    

big_q = 0
second = 0
second_q = 0
for i in range(n):
  if max(arr) == arr[i]:
    big_q += 1
  else:
    if arr[i-1] == max(arr):
      second = arr[i]
    if second != arr[i]:
      break
    else:
      second_q += 1

if big_q == 1 and second_q > 1:
  print(second - minimum_num)
else:
  print(max(arr) - min(arr))