from typing import List

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index1 = 0
        index2 = 0
        turn = True
        res = ""
        while index1 < len(word1) and index2 < len(word2):
            if turn:
                res += word1[index1]
                turn = False
                index1 += 1
            else:
                res += word2[index2]
                turn = True
                index2 += 1

        if index1 < len(word1):
            res += word1[index1:]

        if index2 < len(word2):
            res += word2[index2:]

        return res


if __name__ == '__main__':
    w1 = "abcd"
    w2 = "pq"
    s1 = Solution()
    print(s1.mergeAlternately(w1, w2))
