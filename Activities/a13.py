cars = "The cars present included Ford, Mercedes, Toyota, BMW, Audi and Renault"
answer = input("Enter a make of a car: ").capitalize()

if answer in cars or answer == "Bmw":
    print("It is present")
else:
    print("It is not present")
