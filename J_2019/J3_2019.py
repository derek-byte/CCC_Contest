N = int(input())

for num in range(N):
    string = input()

    i = 0
    ans = ""
    diff_char = string[i]
    char_quan = 0
    while i < len(string):
        if string[i] != diff_char:
            ans += str(char_quan) + " " + diff_char + " "
            diff_char = string[i]
            char_quan = 0

        else:
            char_quan += 1
            i += 1
    ans += str(char_quan) + " " + diff_char + " "
    print(ans)
