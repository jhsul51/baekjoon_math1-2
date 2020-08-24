h = list()
for i in range(15):
    h.append([0]*14)

def household(floor, room):
    global h
    if h[floor][room-1] != 0:
        return h[floor][room-1]
    else:
        if floor == 0:
            h[0][room-1] = room
            return h[floor][room-1]
        else:
            for i in range(1,room+1):
                h[floor][room-1] += household(floor-1,i)
            return h[floor][room-1]

n = int(input())
for i in range(n):
    floor = int(input())
    room = int(input())
    print(household(floor,room))