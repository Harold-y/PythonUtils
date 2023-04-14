
class Solution:
    def longestContinuousChar(self, s: str) -> int:
        matrix = [0] * 26
        for character in s:
            matrix[ord(character) - 97] += 1
        return max(matrix)


if __name__ == '__main__':
    s1 = Solution()
    print(s1.longestContinuousChar("aabaa"))
