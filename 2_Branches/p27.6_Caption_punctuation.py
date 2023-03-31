"""A user is asked to type a caption for a photo in a web form's text field. If the caption didn't end with a
punctuation mark (. ! ?), a period should automatically be added. A common error is to end with a comma, which should
be replaced by a period. Another common error is to end with two periods, which should be changed to one period (
however, ending with three periods (or more) indicates elipses so should be kept as is). The corrected caption is
output.

If the input is "I like pie", the output is "I like pie." If the input is "I like pie!", the output remains "I like
pie!" If the input is "Coming soon…", the output remains "Coming soon…"
"""

photoCap = input("type the caption")
lastChar = photoCap[-1]

if lastChar in '!?':
    pass
elif lastChar == ',':
    photoCap = photoCap[:-1] + '.'
elif lastChar not in '.!?...':
    photoCap += '.'
elif photoCap.endswith('..') and not photoCap.endswith('...'):
    photoCap = photoCap[:-1]

print(photoCap)
