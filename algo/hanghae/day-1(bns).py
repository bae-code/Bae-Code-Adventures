from collections import Counter


def solve():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    if len(nums) == k:
        return nums
    map = dict()
    for n in nums:
        map[n] = map.get(n, 0) + 1
    bucket = [[] for _ in range(len(nums) + 1)]

    for n, v in map.items():
        bucket[v].append(n)
    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            res.append(num)
            if len(res) == k:
                return res


print(solve())

a = list()
