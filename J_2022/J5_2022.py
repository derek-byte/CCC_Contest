arr= []

N = int(input())
for row in range(N):
    arr.append([0]*N)

T = int(input())

for tree in range(T):
    cord = input()
    splitted = cord.split()
    x = int(splitted[0]) -1
    y = int(splitted[1]) -1 
    
    arr[x][y] = 1

def solution(arr):
    dimension = N 
    while dimension != 0:
        i = 0
        while i < len(arr) - (dimension-1):
            j = 0
            while j < len(arr[i]) - (dimension-1):

                # Check custom box
                counter = 0
                if counter == (dimension^2):
                    return dimension
                k = i
                while k < dimension:
                    l = j
                    while l < dimension:
                        if arr[k][l] == 0:
                            counter += 1
                        l += 1
                    k += 1
                
                # if counter == (dimension^2):
                #     return dimension

                j += 1
            i += 1
        dimension -= 1

print(solution(arr))