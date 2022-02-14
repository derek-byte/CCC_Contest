length = int(input())

for num in range(length):
    l = input()
    line = l.split(" ")

    x = int(line[0])
    y = line[1]

    print(y*x)