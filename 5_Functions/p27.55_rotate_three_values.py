def rotate_right(p1,p2,p3):
    tmp = p3
    p3 = p2
    p2 = p1
    p1 = tmp
    print(p1, p2, p3)


p1, p2, p3 = [int(x) for x in input().split()]

rotate_right(p1, p2, p3)

