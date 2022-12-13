def main():
    a = 10
    b = 20
    print(add(a, b))
    hi = add
    print(hi(1, 2))


def add(a, b):
    rst = a + b
    return rst


main()
