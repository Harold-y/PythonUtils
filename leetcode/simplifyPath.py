class Solution:
    def simplifyPath(self, path: str) -> str:
        retPath = ""
        stack = []
        temp = []
        isSlash = False
        for character in path:
            if character == '/':
                if isSlash:
                    continue
                else:
                    isSlash = True
                    if len(temp) > 0:
                        last_item = "".join(temp)
                        if last_item == ".":
                            temp = []
                            continue
                        if last_item == "..":
                            if len(stack) > 0:
                                stack.pop()
                        else:
                            stack.append(last_item)
                    temp = []
            else:
                temp.append(character)
                isSlash = False

        if len(temp) > 0:
            if len(temp) > 0:
                last = "".join(temp)
                if last == "..":
                    if len(stack) > 0:
                        stack.pop()
                elif last != '.':
                    stack.append(last)

        if len(stack) == 0:
            return "/"

        for item in stack:
            retPath += "/" + item

        return retPath


if __name__ == '__main__':
    solution1 = Solution()
    print(solution1.simplifyPath("/c/d//././/.."))