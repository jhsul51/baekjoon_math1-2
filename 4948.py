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

while True:
    count = 0
    n = int(input())
    if n == 0:
        break
    for num in range(n+1,2*n+1):
        if prime(num):
            count += 1
    print(count)
