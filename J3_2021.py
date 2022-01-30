# prev_direction = ""

# while True:

#   num = input()
#   if num == "99999":
#     break

#   add = int(num[1]) + int(num[0])

#   if num[0] != "0" and num[1] == "0":
#     if (add % 2) == 1:
#       direction = "left"
#     else:
#       direction = "right"
#     prev_direction = direction 

#   else:
#     direction = prev_direction

#   print(direction, num[2:])


prev_direction = ""

while True:

  num = input()
  if num == "99999":
    break

  add = int(num[1]) + int(num[0])

  if (add % 2) == 1:
    direction = "left"
  elif num[0] == "0" and num[1] == "0":
    direction = prev_direction 
  else:
    direction = "right"
  prev_direction = direction 

  print(direction, num[2:])




#Andrew's solution 
# inputSequence = input()
# steps = []
# directions = []
# while inputSequence != "99999":
#   twoDigitSum = int(inputSequence[0])+int(inputSequence[1])
#   if twoDigitSum == 0:
#     directions.append(directions[-1])
#   elif twoDigitSum % 2 == 0:
#     # Even
#     directions.append("right")
#   else:
#     directions.append("left")
#   steps.append(inputSequence[2:])
#   inputSequence = input()

# for i in range(len(steps)):
#   print(directions[i], steps[i])

