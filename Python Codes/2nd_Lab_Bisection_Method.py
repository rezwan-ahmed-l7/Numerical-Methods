def f(x):
    return x**3 + x**2 + x + 7


a = -3
b = -2
tol = 0.00005


def bisection(a, b, tol):

    # Check validity
    if f(a) * f(b) >= 0:
        print("Invalid Interval")
        return None

    # Table heading
    print(
        f"{'Iteration':<12}{'a':<12}{'b':<12}{'f(a)':<12}{'f(b)':<12}{'c':<12}{'f(c)':<12}"
    )
    print("-" * 82)

    iter_count = 1

    while (b - a) > tol:

        c = (a + b) / 2

        fa = f(a)
        fb = f(b)
        fc = f(c)

        # Print values
        print(
            f"{iter_count:<12}{a:<12.4f}{b:<12.4f}{fa:<12.4f}{fb:<12.4f}{c:<12.4f}{fc:<12.4f}"
        )

        # Root check
        if fc == 0:
            return c

        # Update interval
        elif fa * fc < 0:
            b = c
        else:
            a = c

        iter_count += 1

    return (a + b) / 2


# Function call
root = bisection(a, b, tol)

if root is not None:
    print(f"\nRoot is: {root:.6f}")
