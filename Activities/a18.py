# Initialization
scores = [
    ["Alexis", 1, 19],
    ["Seema", 1, 29],
    ["Seema", 2, 44],
    ["Lois", 1, 10],
    ["Alexis", 2, 17],
    ["Alexis", 3, 36],
    ["Dion", 1, 23],
    ["Emma", 1, 27],
    ["Emma", 2, 48],
]

# Dictionary for easier data storage
highest = {}

# Get the highest score in every level
for i in range(len(scores)):
    level, score = scores[i][1], scores[i][2]
    if level not in highest:
        highest[level] = score
    elif highest[level] < score:
        highest[level] = score

# Print scores
for i in highest:
    for j in range(len(scores)):
        if highest[i] == scores[j][2] and i == scores[j][1]:
            print(f"Level-{i} = {scores[j][0]}, {highest[i]}")
