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

while True:
    count = 0
    n = int(input())
    if n == 0:
        break
    print(len([i for i in prime(2*n) if i>n]))
    
