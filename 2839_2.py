n = int(input())
m = n//5
k = n%5
while m>=0:
    if k%3 == 0:
        break
    else:
        m -= 1
        k += 5
if m<0:
    print(-1)
else:
    print(m + k//3)