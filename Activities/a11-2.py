calculating = True
while calculating:

    # Ask user of inputs
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operator (+,-,*,/): ")
    num2 = float(input("Enter the second number: "))

    # Perform operation according to the input
    if op == "+":
        print(f"result = {num1 + num2}")
    elif op == "-":
        print(f"result = {num1 - num2}")
    elif op == "/":
        print(f"result = {num1 / num2}")
    elif op == "*":
        print(f"result = {num1 * num2}")
    else:
        print("Invaild operator")

    # If input is neither yes nor no, then prompt again
    while True:

        # Prompt for another calculation
        calculate_again = input(
            "Do you want to perform another calculation: ")

        # Start again if yes, and stop if no
        if calculate_again.upper() == "NO":
            calculating = False
            break
        elif calculate_again.upper() == "YES":
            calculating = True
            break
