def isPossible(stones, k, mid):
    count = 0
    for stone in stones:
        if stone - mid <= 0:
            count += 1
        else:
            count = 0

        if count >= k:
            return False
    return True

def solution(stones, k):
    copy = sorted(stones)

    low, high = 1, copy[-1]

    while low <= high:
        mid = (low + high) // 2
        if isPossible(stones, k, mid):
            low = mid + 1
        else:
            high = mid - 1

    return low
