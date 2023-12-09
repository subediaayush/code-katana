import sys


def minTaps(n: int, ranges: [int]) -> int:
    tapReach = [sys.maxsize] * (n + 1)

    for tapIndex, tapRange in enumerate(ranges):
        left = max(0, tapIndex - tapRange)
        right = min(n, tapIndex + tapRange)

        for i in range(left, right + 1):
            tapReach[i] += min(tapReach[i], tapReach[left] + 1)

    # totalReach = 0
    # for reach in tapReach:
        # if reach > 0:
            # totalReach += 1

    return tapReach[n] if tapReach[n] < sys.maxsize else -1, tapReach

print(minTaps(1, [1,2,3]))