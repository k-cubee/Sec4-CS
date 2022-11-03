score = int(input("Enter your score: "))
high_score = int(input("Enter your high score: "))
if score <= high_score:
    print("You haven't beaten your high score.")
else:
    print("You have exceeded your high score.")
