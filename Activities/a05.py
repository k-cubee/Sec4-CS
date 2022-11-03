age = int(input("Enter your age: "))
lessons = 20

if age <= 18:
    print(f"{lessons = }")
else:
    extra_age = age - 18
    lessons += (extra_age * 2)
    print(f"{lessons = }")
