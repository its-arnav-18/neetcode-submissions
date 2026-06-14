class Solution:
    def mergeTwoLists(self, list1, list2):
        list3 = []

        while list1:
            list3.append(list1.val)
            list1 = list1.next

        while list2:
            list3.append(list2.val)
            list2 = list2.next

        list3.sort()

        dummy = ListNode(0)
        current = dummy

        for num in list3:
            current.next = ListNode(num)
            current = current.next

        return dummy.next