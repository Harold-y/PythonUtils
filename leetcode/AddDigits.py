class Solution:
    def addDigits(self, num: int) -> int:
        next_num = 0
        while True:
            if num < 10:
                return num
            while num > 0:
                next_num += num % 10
                num //= 10
            if next_num < 10:
                return next_num
            while next_num > 0:
                num += next_num % 10
                next_num //= 10


if __name__ == '__main__':
    s1 = Solution()
    print(s1.addDigits(38))
