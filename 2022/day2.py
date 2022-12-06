text = open("./values/2022-2", "r").read()
text = text.split("\n")
text = [x.split(" ") for x in text]
sum = 0

for o, p in text:
    if o == "A":
        if p == "X":
            sum += 3+1
        if p == "Y":
            sum += 6+2
        if p == "Z":
            sum += 3

    elif o == "B":
        if p == "X":
            sum += 1
        if p == "Y":
            sum += 3+2
        if p == "Z":
            sum += 6+3

    elif o == "C":
        if p == "X":
            sum += 6+1
        if p == "Y":
            sum += 2
        if p == "Z":
            sum += 3+3

print(sum)
sum = 0

for o, p in text:
    if p == "X":
        if o == "A":
            sum += 3
        if o == "B":
            sum += 1
        if o == "C":
            sum += 2

    if p == "Y":
        sum += 3
        if o == "A":
            sum += 1
        if o == "B":
            sum += 2
        if o == "C":
            sum += 3

    if p == "Z":
        sum += 6
        if o == "A":
            sum += 2
        if o == "B":
            sum += 3
        if o == "C":
            sum += 1


print(sum)

# The winner of the whole tournament is the player with the highest score.
# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
