validNum = False
while validNum == False:
    number = int(input("Please enter a number between 1 and 10: "))
    if number >= 1 and number <= 10:
        validNum = True
print(f"You have entered: {number}")
