l = input()

t = []
n = []

for i in range(int(l)):
    pair = input().split()
    time = pair[0]
    measurement = pair[1]

    t.append(int(time))
    n.append(int(measurement))

# # Sorting
# j = 1
# while j < len(t):

#     if t[j-1] > t[j]:
#         t.insert(j-1, t[j])
#         t.pop(j+1)
#         n.insert(j-1, n[j])
#         n.pop(j+1)
#     j += 1 


running_speed = 0
j = 0
while j < len(t):
    k = 1
    while k < len(t):
        time = abs(t[k] - t[j])
        distance = abs(n[k] - n[j])

        if time != 0:
            ans = distance / time

        if ans > running_speed:
            running_speed = ans
        k += 1
    j += 1

print(running_speed) 

# n = int(input())

# times_pos = []
# for i in range(n):
#     pair = [int(val) for val in input().split(" ")]
#     times_pos.append(pair)
# times_pos.sort()

# maxS = 0
# for i in range(n-1):
#     speed = abs(times_pos[i][1] - times_pos[i+1][1]) / abs(times_pos[i][0] - times_pos[i+1][0])
#     maxS = max(maxS, speed)
# print(maxS)
