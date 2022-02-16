x = int(input())

array = []
for i in range(x):
    if (x-i) not in array and (x-i) <= 5 and i <=5:
        array.append(x-i)
        array.append(i)

print(int((len(array))/2))
