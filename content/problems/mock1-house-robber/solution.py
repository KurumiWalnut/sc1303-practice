def max_non_adjacent(nums):
    # best_before_prev = best total using houses up to i - 2
    # best_prev        = best total using houses up to i - 1
    best_before_prev, best_prev = 0, 0
    for money in nums:
        # either skip this house, or take it plus the best from two houses back
        best_before_prev, best_prev = best_prev, max(best_prev, best_before_prev + money)
    return best_prev
