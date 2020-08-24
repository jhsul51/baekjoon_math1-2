def household(floor, room):
    people = 0
    if floor == 0:
        return room
    elif floor == 1:
        return room*(room+1)//2
    else:
        for i in range(1,room+1):
            people += household(floor-1,i)
        return people

n = int(input())
for i in range(n):
    floor = int(input())
    room = int(input())
    print(household(floor,room))