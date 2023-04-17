from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = -1
        candyReturn = [False] * len(candies)
        for item in candies:
            if greatest < item:
                greatest = item
        threshold = greatest - extraCandies
        for i in range(0, len(candies)):
            if candies[i] >= threshold:
                candyReturn[i] = True
        return candyReturn
