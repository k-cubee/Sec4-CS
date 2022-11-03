import random


parkCharge = random.randint(0, 20)
payment = 0
while payment < parkCharge or payment > 20:
    print(f"{parkCharge = }")
    print("Enter payment up to $20")
    payment = int(input("payment: "))
    changeDue = payment - parkCharge

    while changeDue >= 10:
        print("$10")
        changeDue -= 10

    while changeDue >= 5:
        print("$5")
        changeDue -= 5

    while changeDue >= 2:
        print("$2")
        changeDue -= 2

    print(f"{changeDue = }")
