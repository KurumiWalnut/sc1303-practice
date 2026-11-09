def subsets(nums):
    out, chosen = [], []

    def go(i):
        if i == len(nums):
            out.append(chosen[:])     # a copy: chosen keeps changing
            return
        go(i + 1)                     # skip nums[i]
        chosen.append(nums[i])        # take nums[i]
        go(i + 1)
        chosen.pop()                  # undo the choice

    go(0)
    return out
