instruc = input()

# if len(instruc) > 11:
#     print("AFB tig")

sep = ""
num = ""
i = 0
while i < len(instruc):
    if instruc[i] == "+" or instruc[i] == "-":
        if instruc[i] == "+":
            order = "tighten"
        elif instruc[i] == "-":
            order = "loosen"


        j = i + 1
        try:
            i += 1
            while int(instruc[i]) == int(instruc[i]):
                # num += instruc[i]
                i += 1
        except:
            pass

        # sep += instruc[i+1]
        i += 1
        print(sep, order, instruc[j:i-1])

        sep=""
        i -= 1

    else:
        sep += instruc[i]
        i += 1