from typing import List
from queue import PriorityQueue


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {
            x: {} for x in range(n)
        }
        for i in range(len(edges)):
            graph[edges[i][0]][edges[i][1]] = succProb[i]
            graph[edges[i][1]][edges[i][0]] = succProb[i]

        visited = set()
        pq = PriorityQueue()
        pq.put((-1.00, start_node))
        while pq.qsize() > 0:
            curr_prob, curr = pq.get()
            if curr == end_node:
                return curr_prob * -1.00
            visited.add(curr)
            for neighbor in graph[curr].keys():
                prob = graph[curr][neighbor]
                if neighbor not in visited:
                    pq.put((prob * curr_prob, neighbor))
        return 0.00


if __name__ == '__main__':
    s1 = Solution()
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2
    print(s1.maxProbability(n, edges, succProb, start, end))
