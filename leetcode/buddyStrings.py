class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        num_diff = 0
        same = 0
        diff_a, diff_b, same_set = set(), set(), set()
        same_fulfilled = False
        for i in range(len(s)):
            c1, c2 = s[i], goal[i]
            if c1 != c2:
                num_diff += 1
                if num_diff > 2:
                    return False
                if c1 in diff_b and c2 in diff_a:
                    diff_b.remove(c1)
                    diff_a.remove(c2)
                else:
                    diff_a.add(c1)
                    diff_b.add(c2)
            else:
                same += 1
                if c1 in same_set:
                    same_fulfilled = True
                same_set.add(c1)
        if len(diff_a) > 0:
            return False
        if num_diff == 2:
            return True
        if num_diff == 1 or (not same_fulfilled):
            return False
        return True


if __name__ == '__main__':
    s1 = Solution()
    print(s1.buddyStrings("abcab", "abcba"))
