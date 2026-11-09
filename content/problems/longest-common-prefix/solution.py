def longest_common_prefix(strs):
    prefix = strs[0]
    for s in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        prefix = prefix[:i]          # the prefix can only get shorter
        if not prefix:
            break
    return prefix
