first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")

if len(last_name) < 4:
    last_name += "X" * (4-len(last_name))
else:
    last_name = last_name[:4]

print(first_name[0] + last_name)
