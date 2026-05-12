def f(x):
    return 1 / (1 + x * x)


def Trapezoidal_rule(x0, xn, n):
    h = (xn - x0) / n
    area = f(x0) + f(xn)

    for i in range(1, n):
        area += 2 * f(x0 + i * h)

    area *= h / 2
    return area


def Simpson_1by3_rule(x0, xn, n):
    if n % 2 != 0:
        print("n must be even for Simpson's 1/3 Rule.")
        return None

    h = (xn - x0) / n
    area = f(x0) + f(xn)

    for i in range(1, n):
        if i % 2 == 0:
            area += 2 * f(x0 + i * h)
        else:
            area += 4 * f(x0 + i * h)

    area *= h / 3
    return area


def Simpson_3by8_rule(x0, xn, n):
    if n % 3 != 0:
        print("n must be a multiple of 3 for Simpson's 3/8      Rule.")
        return None

    h = (xn - x0) / n
    area = f(x0) + f(xn)

    for i in range(1, n):
        if i % 3 == 0:
            area += 2 * f(x0 + i * h)
        else:
            area += 3 * f(x0 + i * h)

    area *= (3 * h) / 8
    return area


a, b, n = 0, 1, 6

area1 = Trapezoidal_rule(a, b, n)
area2 = Simpson_1by3_rule(a, b, 6)
area3 = Simpson_3by8_rule(a, b, 6)

print("\nNumerical Integration")
print(f"Exact Trapezoidal Area : {area1:.6f}")
print(f"Exact Simpson 1/3 Area : {area2:.6f}")
print(f"Exact Simpson 3/8 Area : {area3:.6f}")
