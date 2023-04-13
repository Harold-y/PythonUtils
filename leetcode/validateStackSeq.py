from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for i in range(0, len(pushed)):
            if j < len(popped) and popped[j] == pushed[i]:
                j += 1
                while len(stack) > 0 and j < len(popped) and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
            else:
                stack.append(pushed[i])

        while len(stack) > 0 or j < len(popped):
            if len(stack) <= 0 or j >= len(popped):
                return False
            curr = stack.pop()
            if curr != popped[j]:
                return False
            else:
                j += 1

        return True


if __name__ == '__main__':
    p1 = [2, 1, 0]
    p2 = [1, 2, 0]
    s1 = Solution()
    print(s1.validateStackSequences(p1, p2))
