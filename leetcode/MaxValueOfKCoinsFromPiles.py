import functools
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @functools.lru_cache(None)
        def dp(i, K):
            if K == 0 or i == len(piles): return 0
            res, cur = dp(i + 1, K), 0
            for j in range(min(len(piles[i]), K)):
                cur += piles[i][j]
                res = max(res, cur + dp(i + 1, K - j - 1))
            return res

        return dp(0, k)


if __name__ == '__main__':
    piles = [[1, 100, 3], [7, 8, 9]]
    k = 2
    s1 = Solution()
    print(s1.maxValueOfCoins(piles, k))
