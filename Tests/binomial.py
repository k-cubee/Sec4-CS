import math


c1 = float(eval(input("Enter first coefficient: ")))
c2 = float(eval(input("Enter second coefficient: ")))
power = float(eval(input("Enter power: ")))
index = 0
fr_count = 0

while index != power + 1 or power == -1:
    coef = 1
    first_coef = c1 ** (power-index)
    second_coef = c2 ** index

    for i in range(index):
        coef *= (power - i)

    coef /= math.factorial(index)
    rst = round(first_coef * second_coef * coef, 10)
    index += 1

    if ((power % 2 != 0 and power % 2 != 1) or power <= -1) and index == 7:
        print("...")
        break
    elif ((power % 2 != 0 and power % 2 != 1) or power <= -1) and index != 7:
        print(f"{rst}x^{fr_count}", end="")
    else:
        print(f"{rst}x^{int(power-index+1)}y^{int(index-1)}", end="")

    if index != power + 1:
        print(end=" + ")
    else:
        print()

    fr_count += 1
