M = int(input())
N = int(input())

array = []

# Create table using nested lists
for colum in range(N):
    num_row = []
    for row in range(M):
        num_row.append(0)
    array.append(num_row)

K = int(input())
for order in range(K):
    direction = input()

    arr_direct = direction.split(" ")

    column_row = int(arr_direct[1])

    if arr_direct[0] == "R":
        i = 0
        for num in array[column_row - 1]: 
            if num == 0:
                change = 1
            else:
                change = 0
            array[column_row - 1].insert(i,change)
            array[column_row - 1].pop(i+1)
            i += 1
    else:
        i = 0
        while i < len(array):
            if array[i][column_row - 1] == 0:
                change = 1
            else:
                change = 0
            array[i].insert(column_row - 1,change)
            array[i].pop(column_row)
            i += 1

gold = 0
j = 0    
while j < len(array):
    h = 0
    while h < len(array[j]):
        if array[j][h] == 1:
            gold += 1
        h += 1 
    j += 1

print(gold)