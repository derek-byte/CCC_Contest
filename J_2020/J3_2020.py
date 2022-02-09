N = int(input())

x_arr = []
y_arr = []

for num in range(N):
    inp = input()
    coord = inp.split(",")

    x = coord[0]
    y = coord[1]

    x_arr.append(int(x))
    y_arr.append(int(y))

low_x = x_arr[0]
high_x = x_arr[0]
for num_x in x_arr:
    if num_x < low_x:
        low_x = num_x
    if num_x > high_x:
        high_x = num_x

low_y = y_arr[0]
high_y = y_arr[0]
for num_y in y_arr:
    if num_y < low_y:
        low_y = num_y
    if num_y > high_y:
        high_y = num_y

low_y -= 1
high_y += 1
low_x -= 1
high_x += 1

print(str(low_x) +","+str(low_y))
print(str(high_x) +","+str(high_y))