import math
M = int(input())
N = int(input())
prime = list()
count = 0
for num in range(M,N+1):
    flag = 1
    if num == 1:
        flag = 0
    for i in range(2,math.floor(math.sqrt(num))+1):
        if num%i == 0:
            flag = 0
            break
    if flag == 1:
        prime.append(num)
if not prime:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))