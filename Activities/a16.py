firstNames = ["Ashura", "Bryn", "Eloise", "Mei", "James", "Irena"]
searchName = input("Enter a first name: ")
found = False
index = 0

while not found and index <= len(firstNames) - 1:
    if searchName == firstNames[index]:
        found = True
    index += 1

if found:
    print(f"{searchName} is at position {index} in the list")
else:
    print(f"{searchName} is not in the list")
