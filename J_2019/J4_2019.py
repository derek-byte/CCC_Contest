order = input()

array = [[1,2],[3,4]]

for i in order:
    if i == "V":
        array[0][0], array[0][1] = array[0][1], array[0][0]
        array[1][0], array[1][1] = array[1][1], array[1][0]

    else:
        array[1][0], array[0][0] = array[0][0], array[1][0]
        array[1][1], array[0][1] = array[0][1], array[1][1]

print(array[0][0], array[0][1])
print(array[1][0], array[1][1])