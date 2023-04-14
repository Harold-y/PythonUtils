class Solution:
    def longestPalindromeSubsequence(self, s: str) -> int:
        matrix = [[1] * len(s) for i in range(0, len(s))]
        for step in range(1, len(s)):
            start = 0
            while (start + step) < len(s):
                end = start + step
                if s[start] == s[end]:
                    if step == 1:
                        increment = 0
                    else:
                        increment = matrix[start + 1][end - 1]
                    matrix[start][end] = 2 + increment
                else:
                    matrix[start][end] = max(matrix[start][end - 1], matrix[start + 1][end])
                start += 1

        return matrix[0][len(s) - 1]


if __name__ == '__main__':
    s1 = Solution()
    print(s1.longestPalindromeSubsequence("bbbab"))
