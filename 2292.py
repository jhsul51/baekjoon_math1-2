x = int(input())
n = 1
while True:
    if x <= 1+3*n*(n-1):
        break
    n += 1
print(n)
