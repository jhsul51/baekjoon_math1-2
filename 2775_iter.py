n = int(input())
for i in range(n):
    floor = int(input())
    room = int(input())
    
    h = list()
    for i in range(15):
        h.append([0]*14)
    
    for f in range(floor+1):
        for r in range(room):
            if f==0:
                h[f][r] = r+1
            else:
                h[f][r] = sum(h[f-1][:r+1])
    print(h[floor][room-1])