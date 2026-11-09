def hash_key(key):
    """A simple hash that is the same on every run: ints hash to themselves, strings by their characters."""
    if isinstance(key, int):
        return key
    h = 0
    for ch in str(key):
        h = (h * 31 + ord(ch)) % 1_000_000_007
    return h
