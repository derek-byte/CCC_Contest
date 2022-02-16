X = int(input())
same_group = []
diff_group = []
groups = []
for i in range(X):
    text = input()
    same_group.append(text.split())

Y = int(input())
for i in range(Y):
    text = input()
    diff_group.append(text.split())

g = int(input())
for i in range(g):
    temp = input().split()
    groups.append({temp[0],temp[1],temp[2]})

i = 0
check_group = {}
for location, group in enumerate(groups):
    for student in group:
        check_group[student]= location
for same_person in same_group:
    if check_group[same_person[0]] != check_group[same_person[1]]:
        i+=1
for diff_person in diff_group:
    if check_group[diff_person[0]] == check_group[diff_person[1]]:
        i+=1
print(i)