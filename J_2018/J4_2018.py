num_input = int(input())

sun_flower = []

for i in range(num_input):
    pair = [int(val) for val in input().split(" ")]
    sun_flower.append(pair)

while True:
    if sun_flower[0][0] > sun_flower[0][1] or sun_flower[0][0] > sun_flower[1][0]:
        # Rotate array
        sun_flower = list(zip(*sun_flower[::-1]))
    else:
        break

for i in sun_flower:
    print(i)

# import string


# N = int(input())

# ans = []
# one_location = 0

# for num in range(N):
#     l = input()
#     for i in l:
#         if i ==" ":
#             pass
#         else:
#             ans.append(int(i))

# one = True
# while one:
#     if 


# for j in ans:
#     string_ans = ""
#     for k in range(N):
#         string_ans += str(k)
#         string_ans += " "
#     print(string_ans[0:-1])
