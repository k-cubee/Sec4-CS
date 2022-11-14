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
    level, score = scores[i][2], scores[i][1]
    if str(scores[i][1]) not in highest:
        highest[scores[i][1]] = scores[i][2]
    elif highest[scores[i][1]] > scores[i][2]:
        highest[scores[i][1]] = scores[i][2]

# Print scores
for i in highest:
    print(f"Level-{i} = {highest[i]}")
