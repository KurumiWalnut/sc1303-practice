def remove_duplicates(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()            # the pair cancels
        else:
            stack.append(ch)
    return "".join(stack)
