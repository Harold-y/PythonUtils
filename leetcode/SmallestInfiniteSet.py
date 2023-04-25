import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.to_readd = {}
        self.start = 1

    def popSmallest(self) -> int:
        while self.start in self.heap:
            if self.to_readd.get(self.start) is not None:
                self.to_readd[self.start] = None
                temp = self.start
                self.start += 1
                return temp
            else:
                self.start += 1
        heapq.heappush(self.heap, self.start)
        temp = self.start
        self.start += 1
        return temp

    def addBack(self, num: int) -> None:
        if self.start > num:
            self.start = num
        if num in self.heap:
            self.to_readd[num] = True
