name = input("Enter name: ")
name_length = len(name)

if name_length < 3:
    print("Name must be at least 3 characters")
elif name_length > 30:
    print("Name can be a maximum of 30 characters")
else:
    print("Looks good")
