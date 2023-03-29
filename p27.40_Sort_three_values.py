def ascend_3(a, b, c):
    asc_list = [a, b, c]

    mini = a
    maxi = a
    for x in asc_list:
        if x > maxi:
            maxi = x
        if x < mini:
            mini = x

    mid = a + b + c - mini - maxi

    return mini, mid, maxi


items = [int(x) for x in input().split()]

print(ascend_3(*items))
