from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            if stone2 != stone1:
                heapq.heappush(heap, min(stone2, stone1) - max(stone2, stone1))

        if len(heap) == 0:
            return 0
        else:
            return abs(heap[0])


if __name__ == '__main__':
    s1 = Solution()
    print(s1.lastStoneWeight([3, 7, 2]))
