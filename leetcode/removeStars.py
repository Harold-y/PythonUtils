class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for character in s:
            if character == '*':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(character)
        return "".join(stack)


if __name__ == '__main__':
    s1 = Solution()
    print(s1.removeStars("erase*****"))
