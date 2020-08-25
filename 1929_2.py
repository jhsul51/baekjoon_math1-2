import math
M,N = map(int, input().split())
numlst = list(range(M,N+1))
if 1 in numlst:
    numlst.remove(1)
for i in range(2,math.floor(math.sqrt(N+1))+1):
    for num in numlst:
        if num%i == 0 and num != i:
            numlst.remove(num)
for num in numlst:
    print(num)
