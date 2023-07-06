from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        length = len(nums)
        max_num_subseq = 0
        matrix = [{} for i in nums]
        for i in range(1, length):
            for j in range(0, i):
                diff = nums[j] - nums[i]
                matrix[i][diff] = matrix[j].get(diff, 0) + 1
                max_num_subseq = max(max_num_subseq, matrix[i][diff])

        return max_num_subseq + 1


if __name__ == '__main__':
    s1 = Solution()
    arr = [12, 28, 13, 6, 34, 36, 53, 24, 29, 2, 23, 0, 22, 25, 53, 34, 23, 50, 35, 43, 53, 11, 48, 56, 44, 53, 31, 6,
           31, 57, 46, 6, 17, 42, 48, 28, 5, 24, 0, 14, 43, 12, 21, 6, 30, 37, 16, 56, 19, 45, 51, 10, 22, 38, 39, 23,
           8, 29, 60, 18]
    print(s1.longestArithSeqLength(arr))
