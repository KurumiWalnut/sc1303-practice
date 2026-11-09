def find_circle_num(is_connected):
    n = len(is_connected)
    seen = [False] * n
    provinces = 0
    for start in range(n):
        if seen[start]:
            continue
        provinces += 1
        seen[start] = True
        stack = [start]
        while stack:
            city = stack.pop()
            for other in range(n):
                if is_connected[city][other] and not seen[other]:
                    seen[other] = True
                    stack.append(other)
    return provinces
