from typing import List
from collections import deque
from copy import deepcopy


class Solution:

    def bfs_helper(self, matrix):
        num_row = len(matrix)
        num_col = len(matrix[0])
        visited = set()
        to_visit = deque()
        for i in range(num_col):
            if matrix[0][i] != 1:
                visited.add((0, i))
                to_visit.append((0, i))
        while len(to_visit) > 0:
            curr = to_visit.pop()
            row, col = curr
            if row == num_row - 1:
                return True
            if row - 1 >= 0 and matrix[row - 1][col] == 0 and (row - 1, col) not in visited:
                to_visit.append((row - 1, col))
                visited.add((row - 1, col))
            if col - 1 >= 0 and matrix[row][col - 1] == 0 and (row, col - 1) not in visited:
                to_visit.append((row, col - 1))
                visited.add((row, col - 1))
            if row + 1 < num_row and matrix[row + 1][col] == 0 and (row + 1, col) not in visited:
                to_visit.append((row + 1, col))
                visited.add((row + 1, col))
            if col + 1 < num_col and matrix[row][col + 1] == 0 and (row, col + 1) not in visited:
                to_visit.append((row, col + 1))
                visited.add((row, col + 1))
        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        high = row * col
        low = 0
        mid = abs(high - low) // 2
        last_two = []
        while high - low > 1:
            matrix = [[0 for i in range(col)] for j in range(row)]
            for i in range(mid):
                wet_land = cells[i]
                matrix[wet_land[0] - 1][wet_land[1] - 1] = 1
            if self.bfs_helper(matrix):
                last_two.append(mid)
                low = mid
                mid = abs(high + low) // 2
            else:
                high = mid
                mid = abs(high + low) // 2
        if high - low == 1 and mid == low:
            matrix = [[0 for i in range(col)] for j in range(row)]
            for i in range(high):
                wet_land = cells[i]
                matrix[wet_land[0] - 1][wet_land[1] - 1] = 1
            if self.bfs_helper(matrix):
                last_two.append(high)

        return max(last_two)


if __name__ == '__main__':
    s1 = Solution()
    r = 2
    c = 6
    procedure = [[1, 4], [1, 3], [2, 1], [2, 5], [2, 2], [1, 5], [2, 4], [1, 2], [1, 6], [2, 3], [2, 6], [1, 1]]
    print(s1.latestDayToCross(r, c, procedure))
