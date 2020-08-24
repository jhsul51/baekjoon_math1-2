import sys
T = int(input())
for i in range(T):
    H,W,N = map(int,sys.stdin.readline().split())
    N -= 1
    print("%d%02d" %(N%H+1,N//H+1))