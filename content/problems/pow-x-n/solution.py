def my_pow(x, n):
    if n < 0:
        return 1 / my_pow(x, -n)
    if n == 0:
        return 1.0
    half = my_pow(x, n // 2)              # one call, used twice
    if n % 2 == 0:
        return half * half
    return x * half * half
