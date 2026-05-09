import math


def f(x):
    return 3 * x - math.cos(x) - 1


def g(x):
    return (1 + math.cos(x)) / 3


x0 = 3.2
tol = 0.0005


def iteration(x0, tol, max_iter=100):
    print(f"{'Iteration':<12}{'x':<12}{'f(x)':<12}")
    print("-" * 40)
    i = 1
    while i <= max_iter:
        x1 = g(x0)
        fx = f(x1)
        print(f"{i:<12}{x1:<12.6f}{fx:<12.6f}")

        if abs(x1 - x0) < tol:
            print(f"\nRoot is approximately: {x1:.6f}")
            return
        x0 = x1
        i += 1
    print("\nDid not converge within max iterations.")


iteration(x0, tol)
