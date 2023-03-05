n = ''.join(sorted(input()))[::-1]
n2 = ''.join(sorted(input()))[::-1]

# print(n, n2)

a = 0
m = 0
i = 0
while i < len(n2):
  if n[i] != n2[i-m]:
    if n2[i] == "*":
      a += 1
    m += 1
  i += 1

for i in range(len(n2)-(m-a), len(n2)):
  if n2[i] == "*":
    a += 1

if a == m:
  print("A")
else:
  print("N")









# print(''.join(sorted(n)), ''.join(sorted(n2)))

# def solution(n, n2):
#   n2_vals = {}
#   for i in range(len(n2)):
#     if n2[i] not in n2_vals:
#       n2_vals[n2[i]] = 1
#     else:
#       n2_vals[n2[i]] += 1

#   n1_vals = {}
#   for i in range(len(n)):
#     if n[i] not in n1_vals:
#       n1_vals[n[i]] = 1
#     else:
#       n1_vals[n[i]] += 1
      
#   astriks = 0
#   for i, v in enumerate(n1_vals):
#     if v in n2_vals:
#       if n2_vals[v] != n1_vals[v]:
#         astriks += abs(n2_vals[v] - n1_vals[v])
#     else:
#       astriks += n1_vals[v]

#   if "*" in n2_vals:
#     if astriks == n2_vals["*"]:
#       return "A"
#     else:
#       print(astriks, n2_vals["*"])
#       return "N"
#   else:
#     if astriks == 0:
#       return "A"
#     else:
#       return "N"
  
# print(solution(n, n2))