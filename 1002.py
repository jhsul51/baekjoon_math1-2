n = int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    a = [r1,r2,d]
    m =max(a)
    a.remove(m)
    if d ==0 and r1 == r2:
        print(-1)
    elif m < sum(a):
        print(2)
    elif m == sum(a):
        print(1)
    else:
        print(0)