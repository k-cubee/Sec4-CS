def main():
    n = float(input("n: "))
    ans = factorial(n)
    print(ans)


def factorial(n):
    if n < 2:
        return 1
    ans = factorial(n - 1)
    ans *= n
    return ans


main()
