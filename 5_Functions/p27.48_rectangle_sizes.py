def is_smaller(r1_xul, r1_yul, r1_xbr, r1_ybr, r2_xul, r2_yul, r2_xbr, r2_ybr):
    r1_area = abs((r1_xbr - r1_xul) * (r1_ybr - r1_yul))
    r2_area = abs((r2_xbr - r2_xul) * (r2_ybr - r2_yul))
    return r1_area < r2_area


r1_xul, r1_yul, r1_xbr, r1_ybr = map(int, input("Enter rectangle 1 coordinates: ").split())
r2_xul, r2_yul, r2_xbr, r2_ybr = map(int, input("Enter rectangle 2 coordinates: ").split())

if is_smaller(r1_xul, r1_yul, r1_xbr, r1_ybr, r2_xul, r2_yul, r2_xbr, r2_ybr):
    print("The first rectangle is smaller")
else:
    print("The second rectangle is smaller or equal.")
