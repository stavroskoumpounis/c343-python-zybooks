"""
Bowling involves 10 frames. Each frame starts with 10 pins. The bowler has two throws to knock all 10 pins down.
The total score is the sum of pins knocked down, with some special rules.

For the first 9 frames:

If all 10 pins are knocked down on a frame's first throw (a "strike"), that frame's score is the previous frame plus
10 plus the next two throws. (No second throw is taken).

If all 10 pins are knocked down after a frame's second throw (a "spare"), that frame's score is the previous frame
plus 10 plus the next throw.

In the 10th frame, if the bowler's first throw is a strike, or the first two throws yields a spare, the bowler gets a
third throw. The 10th frame's score is the previous frame's score plus the pins knocked down in the 10th frame's two
or three throws.

Given integers represents all throws for a game, output on one line each frame's score followed by a space (and end
with a newline). Note that the number of throws may be as few as 11 (strikes in first 9 frames, and no strike/spare
in 10th frame), or as many as 21 (2 throws in first 9 frames, then 3 in 10th).

For simplicity, the input will always have 21 integers. If the game ended with fewer than 21 throws, the remaining
integers will be 0's and can be ignored.

Ex: A perfect game is one where every throw is a strike. The 21 input integers will be: 10 10 10 10 10 10 10 10 10 10
10 10. The output will be: 30 60 90 120 150 180 210 240 270 300.
"""

throws = [int(x) for x in input("Enter the scores: ").split()]

frame_scores = []
throw_i = 0
frame_count = 10

for frame in range(frame_count):
    if throws[throw_i] == 10:  # strike
        score = throws[throw_i] + throws[throw_i + 1] + throws[throw_i + 2]
        throw_i += 1
    elif throws[throw_i] + throws[throw_i + 1] == 10:  # spare
        score = throws[throw_i] + throws[throw_i + 1] + throws[throw_i + 2]
        throw_i += 2
    else:  # open frame
        score = throws[throw_i] + throws[throw_i + 1]
        throw_i += 2

    # Add the score of the current frame to the last frame score
    frame_scores.append(frame_scores[-1] + score if frame_scores else score)

print(" ".join(map(str, frame_scores)))


