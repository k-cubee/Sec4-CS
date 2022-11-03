day = input("Enter the day of the week: ").capitalize()
if day == "Saturday" or day == "Sunday":
    alarm = 11
else:
    alarm = 8
print(alarm)
