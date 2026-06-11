import math


def f(x):
    return 3 * x - math.cos(x) - 1


def df(x):
    return 3 + math.sin(x)


x0 = 1
tol = 0.0005


def newrap(x0, tol, max_i=100):

    i = 1

    while i < max_i:

        fx = f(x0)
        dfx = df(x0)

        x1 = x0 - (fx / dfx)

        print(f"X{i} = {x1:.6f}")

        if abs(x1 - x0) <= tol:
            break

        x0 = x1
        i += 1

    print(f"\nRoot is : {x1:.4f}")


newrap(x0, tol)
