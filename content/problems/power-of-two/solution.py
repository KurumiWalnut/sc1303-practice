def is_power_of_two(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 == 1:
        return False
    return is_power_of_two(n // 2)
