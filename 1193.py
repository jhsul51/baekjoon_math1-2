x = int(input())
row = 1
order = 0
while True:
    if row*(row+1)/2 >= x:
        order = x - (row-1)*row/2
        if row%2 == 0:
            print("%d/%d" %(order,(row+1-order)))
        else:
            print("%d/%d" %((row+1-order),order))
        break
    row += 1