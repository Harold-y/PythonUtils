from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        record = {}
        currNode = head
        while currNode is not None:
            if record.get(currNode) is not None:
                return True
            record[currNode] = True
            currNode = currNode.next
        return False
