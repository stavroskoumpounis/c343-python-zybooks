vi = int(input())
t = 0
rocketHeight = vi * t - 5 * t**2
while rocketHeight >= 0:
    print(t, rocketHeight)
    t += 1
    rocketHeight = vi * t - 5 * t**2
