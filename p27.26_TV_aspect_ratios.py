import math

tv_diagonal = float(input())

for tv_width in range(1, int(tv_diagonal)):
    tv_height = math.sqrt(tv_diagonal**2 - tv_width**2)
    if tv_width > tv_height:
        print('{:.0f} {:.1f}'.format(tv_width, tv_height))
