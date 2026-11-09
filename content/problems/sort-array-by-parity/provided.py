def check_parity(result, nums):
    """Return "ok" if result holds the same numbers as nums with every even number before every odd one."""
    if not isinstance(result, list):
        return f"expected a list, got {type(result).__name__}"
    if sorted(result) != sorted(nums):
        return "the result doesn't hold the same numbers as the input"
    for i in range(1, len(result)):
        if result[i - 1] % 2 == 1 and result[i] % 2 == 0:
            return f"odd {result[i - 1]} comes before even {result[i]} at index {i}"
    return "ok"
