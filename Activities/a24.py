highest_score = [20, 50, 100, 30, 40]

with open("scores.txt", "w") as myFile:
    for score in highest_score:
        myFile.write(f"{score}\n")

with open("scores.txt", "r") as myFile:
    new_scores = myFile.read().splitlines()

print(new_scores)
