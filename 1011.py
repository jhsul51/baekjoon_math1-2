import sys
n = int(input())
for i in range(n):
    init, fin = map(int, sys.stdin.readline().split())
    dis = fin - init
    vel = 0
    count = 0
    while True:
        if dis <= (vel+1)*vel:
            if dis > vel*vel:
                count = 2*vel
            else:
                count = 2*vel -1
            break
        vel += 1
    print(count)
