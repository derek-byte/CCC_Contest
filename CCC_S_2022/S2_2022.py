#PARSE
x = int(input())
same_checks = []
diff_checks = []
groups = []
for i in range(x):
    same_checks.append(input().split())
y = int(input())
for i in range(y):
    diff_checks.append(input().split())
g = int(input())
for i in range(g):
    temp = input().split()
    groups.append({temp[0],temp[1],temp[2]})
# SOLVE
v = 0
studg = {}
# find what group each student is in
for group_index,group in enumerate(groups):
    for student in group:
        studg[student]= group_index
# check same_checks
for same_check in same_checks:
    if studg[same_check[0]] != studg[same_check[1]]:
        v+=1
# check different_checks
for diff_check in diff_checks:
    if studg[diff_check[0]] == studg[diff_check[1]]:
        v+=1
print(v)