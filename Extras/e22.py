numbers = [3, 12, 6, 4, 8, 2, 10]
largest = numbers[0]
lowest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < lowest:
        lowest = number

print(f"{largest = }, {lowest = }")
