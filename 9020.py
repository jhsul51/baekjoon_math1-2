def prime(num):
    lis = [True]*(num+1)
    if num == 1:
        return []
    else:
        for i in range(2,int((num+1)**0.5)+1):
            if lis[i] == True:
                for j in range(i+i,num+1,i):
                    lis[j] = False
        pp = list()
        for i in range(2,num+1):
            if lis[i] == True:
                pp += [i]
        return pp

T = int(input())
for i in range(T):
    n = int(input())
    plist = prime(n)
    diff = 100000
    for p in plist:
        if n-p in plist and abs(n-2*p)<diff:
            p1 = p
            p2 = n-p
            diff = abs(n-2*p)
    print(p1,p2)
    # half = (len(plist)-1)//2
    # if plist[half] > n/2:
    #     for j in reversed(range(half+1)):
    #         if n-plist[j] in plist:
    #             print(plist[j],n-plist[j])
    #             break
    # else:
    #     for j in 