def is_valid(s):
    opener_for = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in opener_for:
            # a closer must match the most recent unclosed opener
            if not stack or stack.pop() != opener_for[ch]:
                return False
        else:
            stack.append(ch)
    return not stack                     # anything left open means unbalanced
