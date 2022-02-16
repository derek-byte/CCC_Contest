N = int(input())

swift = input()
sema = input()

l_swift = swift.split(" ")
l_sema = sema.split(" ")

i = 0
t_swift = 0
t_sema = 0
counter = 0
while i < len(l_swift):
    t_sema += int(l_sema[i])
    t_swift += int(l_swift[i])
    if t_sema == t_swift:
        counter = i+1
    i += 1

if counter == len(l_sema):
    print(N)

else:
    print(counter)
