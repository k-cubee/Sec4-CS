print("1. Register as a new user.")
print("2. Login.")
print("3. Change your password.")

while True:
    choice = int(input("Please select a menu option."))
    if choice == 1:
        newUser()
        break
    elif choice == 2:
        login()
        break
    elif choice == 3:
        changePassword()
        break
    elif choice == 4:
        exit()
    else:
        print("Incorrect option. Try again.")
