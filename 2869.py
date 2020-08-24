import sys
A,B,V = map(int,sys.stdin.readline().split())
if A>V:
    print(1)
else:
    if (V-A)%(A-B) != 0:
        day = (V-A)//(A-B) + 2
    else:
        day = (V-A)//(A-B) + 1
    print(day)