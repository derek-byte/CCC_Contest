N = int(input())

point_t = []

for num in range(N):
    points = int(input())
    fouls = int(input())

    point_t.append(points*5 - fouls*3)

count = 0
for i in point_t:
    if i > 40:
        count += 1

plus = ""
if count == N:
    plus = "+"

print(str(count)+plus)