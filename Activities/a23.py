postCode = input("Enter post code: ")
length = len(postCode)
if length >= 6 and length <= 8:
    print("Valid")
else:
    print("Invalid")
