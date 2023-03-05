s = int(input())

same = {}
for i in range(s):
  s = input().split(" ")
  same[s[0]] = s[1]
  same[s[1]] = s[0]

r = int(input())
res = {}
for i in range(r):
  s = input().split(" ")
  res[s[0]] = s[1]
  res[s[1]] = s[0]

g = int(input())
ans = 0
for i in range(g):
  s = input().split(" ")
  for j in range(len(s)):
    if res[s[j]] in s:
      ans += 1
    if s[j] in same:
      if same[s[j]] not in s:
        ans += 1
    
print(ans)