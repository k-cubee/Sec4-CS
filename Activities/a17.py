marks = [
    [80, 59, 34, 89],
    [31, 11, 47, 64],
    [29, 56, 13, 91],
    [55, 61, 48, 0],
    [75, 78, 81, 91],
]
highest = lowest = marks[0][0]
total = count = 0

for i in marks:
    for j in i:
        total += j
        count += 1
        if j > highest:
            highest = j
        if j < lowest:
            lowest = j

print(f"{highest = }, {lowest = }, average = {total / count}")
