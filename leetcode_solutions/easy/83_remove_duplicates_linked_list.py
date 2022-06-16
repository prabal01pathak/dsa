# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = head
        cur = head.next
        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
                cur.next = None
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return head


def test_deleteDuplicates():
    from utils import to_linked_list
    from utils import to_list

    s = Solution()
    head = to_linked_list([1, 2, 3, 3, 4, 4, 5])
    head = s.deleteDuplicates(head)
    assert to_list(head) == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    test_deleteDuplicates()
    print("===================== Test Passed =====================")
