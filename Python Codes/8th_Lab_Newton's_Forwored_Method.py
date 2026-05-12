def forward_diff_table(y):
    n = len(y)
    table = [[0 for _ in range(n)] for _ in range(n)]

    # First column is f(x)
    for i in range(n):
        table[i][0] = y[i]

    # Compute forward differences
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]

    return table


def newton_forward_interpolation(x, y, xi):
    n = len(x)
    h = x[1] - x[0]  # equal spacing assumed
    p = (xi - x[0]) / h

    table = forward_diff_table(y)
    result = y[0]
    p_term = 1

    for i in range(1, n):
        p_term *= p - (i - 1)
        result += (p_term * table[0][i]) / factorial(i)

    return result, table


def factorial(n):
    if n == 0 or n == 1:
        return 1

    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


x = [1891, 1901, 1911, 1921, 1931]
y = [46, 66, 81, 93, 101]
xi = 1895

interpolated_value, table = newton_forward_interpolation(x, y, xi)
print(f"\nNewton Forward Interpolation at x = {xi:.4f} : {interpolated_value:.4f}")
