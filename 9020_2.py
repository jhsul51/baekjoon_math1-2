def prime(num):
    if num == 1 or (num%2==0 and num != 2):
        return False
    elif num ==2:
        return True
    else:
        for i in range(1,(int(num**0.5+1)//2)):
            if num%(2*i+1) == 0:
                return False
        return True

T = int(input())
for i in range(T):
    n = int(input())
    for p in reversed(range(n//2+1)):
        if prime(p) and prime(n-p):
            print(p,n-p)
            break
