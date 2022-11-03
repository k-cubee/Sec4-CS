num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
diff = num2 - num1 + 1
sum = int(diff * 0.5 * (num1 + num2))
print(sum)
sum1 = 0

for i in range(num1, num2 + 1):
    sum1 += i
print(sum1)
