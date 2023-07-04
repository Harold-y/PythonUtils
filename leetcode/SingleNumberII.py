from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashtable = {}
        for num in nums:
            if hashtable.get(num) is None:
                hashtable[num] = 1
            else:
                hashtable[num] += 1
        for key in hashtable.keys():
            if hashtable.get(key) != 3:
                return key


if __name__ == '__main__':
    s1 = Solution()
    print(s1.singleNumber([2, 2, 3, 3]))
