# negative exponents


def n_rec_pow(a, b):
    # handle user error
    try:
        value = int(b)
    except ValueError:
        print("Exponent (b) must be an integer")
        return

    # anything raised to the power of 0 is 1
    if b == 0:
        return 1

    # positive exponent
    elif b > 0:
        # call a multiplied by n_rec_pow on a and b - 1
        return a * n_rec_pow(a, b - 1)
    else:
        # negative exponent
        return 1 / (a * n_rec_pow(a, -b - 1))


print(n_rec_pow(2, -2))
