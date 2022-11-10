code = input("Enter code: ")
if code[0] >= "A" and code[0] <= "I":
    print("Midlands depot")
elif code[0] >= "J" and code[0] <= "R":
    print("South depot")
elif code[0] >= "S" and code[0] <= "Z":
    print("North depot")
else:
    print("Unknown code")
