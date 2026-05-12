def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def backward_diff_table(y):
    n = len(y)
    table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        table[i][0] = y[i]

    for j in range(1, n):
        for i in range(j, n):
            table[i][j] = table[i][j - 1] - table[i - 1][j - 1]

    return table


def newton_backward_interpolation(x, y, xi):
    n = len(x)
    h = x[1] - x[0]
    p = (xi - x[-1]) / h

    table = backward_diff_table(y)

    result = y[-1]
    p_term = 1

    for i in range(1, n):
        p_term *= p + i - 1
        result += (p_term * table[-1][i]) / factorial(i)

    return result, table


# Data
x = [1891, 1901, 1911, 1921, 1931]
y = [46, 66, 81, 93, 101]
xi = 1895

# Run
interpolated_value, table = newton_backward_interpolation(x, y, xi)

print(f"\nNewton Backward Interpolation at x = {xi}: {interpolated_value:.4f}")
