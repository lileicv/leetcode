'''Merge Two Sorted Lists
1->2->3, 1->3->4 ==> 1->1->2->3->3->4
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def genlist(nums):
    li = ListNode(nums[0])
    pt = li
    for i in nums[1:]:
        pt.next = ListNode(i)
        pt = pt.next
    return li

def printlist(nums):
    if nums==None:
        print('None')
        return True
    while True:
        print('{}->'.format(nums.val), end='')
        nums = nums.next
        if nums == None:
            print()
            break

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        head = ListNode(0)
        pt = head
        while True:
            if l1.val > l2.val:
                pt.next = ListNode(l2.val)
                pt = pt.next
                l2 = l2.next
            else:
                pt.next = ListNode(l1.val)
                pt = pt.next
                l1 = l1.next
            if l1==None:
                pt.next = l2
                break
            if l2==None:
                pt.next = l1
                break
        return head.next



a = genlist([1,2,3])
b = genlist([2,3,4])
printlist(a)
printlist(b)

so = Solution()
printlist(so.mergeTwoLists(None,None))

        
