# Compute the factorial of a given value

# multiply all whole number from the given value backward
# up to 1 ) not included

# e.g 1 * 2 * 3 * 4

# iterative approach


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(factorial(4))


def factorial_recursive(n):
    if n == 1:
        return 1

    return n * factorial_recursive(n - 1)


print(factorial_recursive(4))
