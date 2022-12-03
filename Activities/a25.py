highest_score = [
    ['Emily', 20],
    ['Charlie', 50],
    ['Susan', 100],
    ['Mark', 30],
    ['Eve', 40],
]

with open("list.txt", "w") as myFile:
    for score in highest_score:
        myFile.write(f"{score}\n")

with open("list.txt", "r") as myFile:
    new_scores = myFile.read().splitlines()

for i in range(len(new_scores)):
    new_scores[i] = eval(new_scores[i])

print(new_scores)
