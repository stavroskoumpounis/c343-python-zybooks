"""
A university has a web page that displays the instructors for a course, using the following algorithm: If only one
instructor exists, the instructor's first initial and last name are listed. If two instructors exist, only their last
names are listed, separated by /. If three exist, only the first two are listed, with "/ …" following the second. If
none exist, print "TBD". Given six words representing three first and last names (each name a single word; latter
names may be "none none"), output one line of text listing the instructors' names using the algorithm. If the input
is "Ann Jones none none none none", the output is "A. Jones". If the input is "Ann Jones Mike Smith Lee Nguyen" then
the output is "Jones / Smith / …".
"""
name1, surname1, name2, surname2, name3, surname3 = input().split()

if name1 == "none":
    print("TBD")
elif name2 == "none":
    print(f"{name1[0]}. {surname1}")
elif name3 == "none":
    print(f"{surname1} / {surname2}")
else:
    print(f"{surname1} / {surname2} / ...")
