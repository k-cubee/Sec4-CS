def main():
    y = dict()
    x = 0
    i = 0
    graph = input("y = ")

    while x < 1000:
        x = round(x + 0.1, 3)
        y[x] = round(func(x, graph), 3)
        i += 1

    for i in y:
        print(f"{i} = {y[i]}", end=", ")
    print("")


def func(x, graph):
    y = 0
    y = eval(graph)
    return y


main()
