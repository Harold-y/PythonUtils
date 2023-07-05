from typing import List
from collections import deque


class Solution:

    # DP Solution, having matrix size of 2 * N, first row calculates the consecutive num of 1's in ith position
    # second row calculates the consecutive num of 1's backward in ith position
    # if we remove i, then the max # of consecutive 1 is calculated by [0, i - 1] + [1, i + 1]
    # Time complexity: O(n) <- traverse three times, O(3n)
    # Space complexity: O(n)
    def longestSubarray(self, nums: List[int]) -> int:
        forward, backward = [], deque()
        forward.append(nums[0])
        backward.appendleft(nums[len(nums) - 1])
        for i in range(1, len(nums)):
            if nums[i] == 0:
                forward.append(nums[i])
            else:
                forward.append(nums[i] + forward[i - 1])
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                backward.appendleft(nums[i])
            else:
                backward.appendleft(nums[i] + backward[0])
        if len(nums) == 1:
            max_num = 0
        elif len(nums) == 2:
            max_num = max(forward) - 1
        else:
            max_num = max(forward[1], backward[1])
        for i in range(1, len(nums) - 1):
            curr_max = forward[i - 1] + backward[i + 1]
            max_num = max(max_num, curr_max)
        return max_num

    # Jump Zero Solution, having indices of each zero and pushing to the right. Each time we have a zero index, we
    # assume to remove that zero and calculate the consecutive 1's left and right to it, and also get the next zero
    # index.
    # Time complexity: O(n) <- each element is accessed max twice, O(2n)
    # Space complexity: O(1)
    def longestSubarray2(self, nums: List[int]) -> int:
        curr_len = 0
        index_next_zero = -1
        for i in range(0, len(nums)):
            if nums[i] == 0:
                index_next_zero = i
                break
            else:
                curr_len += 1
        max_num = curr_len - 1

        terminate = index_next_zero == -1
        while not terminate:
            left = max(index_next_zero - 1, 0)
            right = min(index_next_zero + 1, len(nums) - 1)
            while left >= 0 and nums[left] != 0:
                left = left - 1
            if left == index_next_zero:
                left -= 1
            while right < len(nums) and nums[right] != 0:
                right = right + 1
            if right >= len(nums) - 1:
                terminate = True
            elif nums[right] == 0:
                index_next_zero = right
            max_num = max(max_num, right - left - 2)

        return max_num


if __name__ == '__main__':
    s1 = Solution()
    seq = [1, 1, 1]
    print(s1.longestSubarray(seq))
    print(s1.longestSubarray2(seq))
