import sys
import math
n = int(input())
numlst = list(map(int,sys.stdin.readline().split()))
count = 0
for num in numlst:
    flag = 1
    if num == 1:
        flag = 0
    for i in range(2,math.floor(math.sqrt(num))+1):
        if num%i == 0:
            flag = 0
            break
    count += flag
print(count)