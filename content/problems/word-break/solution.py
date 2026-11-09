def word_break(s, word_dict):
    words = set(word_dict)
    lengths = {len(w) for w in words}
    n = len(s)
    can = [False] * (n + 1)
    can[n] = True                                 # empty suffix
    for i in range(n - 1, -1, -1):
        can[i] = any(i + k <= n and can[i + k] and s[i:i + k] in words for k in lengths)
    return can[0]
