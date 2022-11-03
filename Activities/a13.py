cars = "The cars present included Ford, Mercedes, Toyota, BMW, Audi and Renault"
answer = input("Enter a make of a car: ").capitalize()

if answer in cars.capitalize():
    print("It is present")
else:
    print("It is not present")
