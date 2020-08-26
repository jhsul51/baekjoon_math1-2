import math
M,N = map(int, input().split())
for num in range(M,N+1):
    flag = 1
    if num == 1:
        flag = 0
    for i in range(2,math.floor(math.sqrt(num))+1):
        if num%i == 0:
            flag = 0
            break
    if flag == 1:
        print(num)
