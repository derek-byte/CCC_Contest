N = int(input())
array = []

for i in range(N): 
  name = input()
  array.append(name)
  bid = int(input())
  array.append(bid)

def silent_auction(array):
  i = 1
  top_bet = 0
  person = ""

  while i < len(array):
    if int(array[i]) > top_bet:
      top_bet = int(array[i])
      person = array[i-1]
    i += 2 
    
  return person

print(silent_auction(array))
