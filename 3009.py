xlist = list()
ylist = list()
for i in range(3):
    x,y = map(int,input().split())
    xlist += [x]
    ylist += [y]

for x in xlist:
    if xlist.count(x) == 1:
        print(x,end=" ")
for y in ylist:
    if ylist.count(y) == 1:
        print(y)