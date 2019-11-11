#test read and process scores

participant_score = {}

f = open("scores.txt", "r")

for line in f:
    entry = line.strip().split(",")
    participant = entry[0]
    score = entry[1]
    participant_score[participant] = score
    print(entry)
    print(participant + " : " + score)

f.close()

print(participant_score)
