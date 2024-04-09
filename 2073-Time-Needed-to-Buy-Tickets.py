from typing import List

class Solution:
    def timeRequiredToBuy(self, v: List[int], k: int) -> int:
        n = len(v)
        value = v[k]
        t = 0
        for i in range(n):
            if i < k:
                t += min(v[i], value)
            elif i == k:
                t += value
            else:
                if v[i] < value:
                    t += v[i]
                else:
                    t += value - 1
        return t