def answer():
    # Variable names are swapped
    cyclic_shift = input()
    text = input()

    i = 0
    while i < len(text):

        j = len(text) 
        k = 0
        while j <= len(cyclic_shift):
            if cyclic_shift[k:j] == text:
                return "yes"
            j += 1 
            k += 1

        # Rotate characters 
        front_text_char = text[0]
        text = text[1::]
        text += front_text_char
        i += 1 
    return "no"

print(answer())

