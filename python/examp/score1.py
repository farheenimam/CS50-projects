#Arrays in python can grow and shrink according to your own will
#They are just like linked listds in C
from cs50 import get_int

scores = []
for i in range (3):
    score = get_int("score:")
    # We can do this append also like this: scores += [score]
    scores.append(score)

average = sum(scores) / len(scores)
print(f"average: {average}")