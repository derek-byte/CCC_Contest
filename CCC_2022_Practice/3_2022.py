N = int(input())

dict = {}
for num in range(N):
    x = int(input())
    if x not in dict:
        dict[x] = 1
    else:
        dict[x] += 1

key_list = list(dict.keys())
key_value = list(dict.values())

low_key = key_list[0]
low_value = 0
high_key = key_list[0]
high_value = 0

for key, value in dict.items():
    if low_key > high_key:
        low_key, high_key = high_key, low_key
        low_value, high_value = high_value, low_value

    if value >= low_value:
        if low_key > key:
            low_key = key
            low_value = value
    if value >= high_value:
        if high_key < key and key != low_key:
            high_key = key
            high_value = value

print(abs(high_key-low_key))