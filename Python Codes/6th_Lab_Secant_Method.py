def f(x):
    return x**3 - 2 * x - 5


a = 2
b = 3
tol = 0.00005
max_iter = 100


def secant(a, b, tol, max_iter):

    print(
        f"{'Iteration':<12}{'a':<12}{'b':<12}{'f(a)':<12}{'f(b)':<12}{'c':<12}{'f(c)':<12}"
    )
    print("-" * 82)

    for i in range(1, max_iter + 1):

        fa = f(a)
        fb = f(b)

        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        print(f"{i:<12}{a:<12.6f}{b:<12.6f}{fa:<12.6f}{fb:<12.6f}{c:<12.6f}{fc:<12.6f}")

        if abs(fc) <= tol:
            return c

        a = b
        b = c

    return c


root = secant(a, b, tol, max_iter)

print(f"\nRoot is : {root:.6f}")
