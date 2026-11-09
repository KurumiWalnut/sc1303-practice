def daily_temperatures(temps):
    answer = [0] * len(temps)
    waiting = []                           # indexes, temperatures never increasing upward
    for i, t in enumerate(temps):
        while waiting and temps[waiting[-1]] < t:
            j = waiting.pop()
            answer[j] = i - j
        waiting.append(i)
    return answer
