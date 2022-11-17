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
    level = scores[i][1]
    name_score = [scores[i][0], scores[i][2]]
    if level not in highest:
        highest[level] = name_score
    elif highest[level][1] < name_score[1]:
        highest[level] = name_score

# Print scores
for i in highest:
    print(f"Level-{i} = {highest[i][0]}, {highest[i][1]}")
