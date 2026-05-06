def f(x):
    return x**3 - 2 * x - 5


a = 2
b = 3
tol = 0.00005
max_iter = 100


def false_position(a, b, tol, max_iter):

    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return None

    print(
        f"{'Iteration':<12}{'a':<12}{'b':<12}{'f(a)':<12}{'f(b)':<12}{'c':<12}{'f(c)':<12}"
    )
    print("-" * 82)

    i = 1

    while i <= max_iter:

        fa = f(a)
        fb = f(b)

        # False Position Formula
        c = (a * fb - b * fa) / (fb - fa)

        fc = f(c)

        print(f"{i:<12}{a:<12.6f}{b:<12.6f}{fa:<12.6f}{fb:<12.6f}{c:<12.6f}{fc:<12.6f}")

        if abs(fc) <= tol:
            return c

        elif fa * fc < 0:
            b = c
        else:
            a = c

        i += 1

    return c


root = false_position(a, b, tol, max_iter)

if root is not None:
    print(f"\nRoot is: {root:.6f}")
