mark1 = int(input("Enter mark1: "))
mark2 = int(input("Enter mark2: "))
mark3 = int(input("Enter mark3: "))

if mark1 > mark2 and mark1 > mark3:
    print(f"{mark1 = }")
elif mark2 > mark1 and mark2 > mark3:
    print(f"{mark2 = }")
elif mark3 > mark1 and mark3 > mark2:
    print(f"{mark3 = }")
else:
    print("All marks are the same.")
