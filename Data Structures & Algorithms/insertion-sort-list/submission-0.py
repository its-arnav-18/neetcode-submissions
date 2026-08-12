# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        arr.sort()
        cur = head
        for val in arr:
            cur.val = val
            cur = cur.next
        return head