'''Remove Nth Node From End of List
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        pt1 = pre
        pt2 = pre
        for i in range(n):
            pt2 = pt2.next

        while pt2.next!=None:
            pt1 = pt1.next
            pt2 = pt2.next

        pt1.next = pt1.next.next
        return pre.next

def genlist(nums):
    li = ListNode(nums[0])
    pt = li
    for i in nums[1:]:
        pt.next = ListNode(i)
        pt = pt.next
    return li

def printlist(nums):
    while True:
        print('{}->'.format(nums.val), end='')
        nums = nums.next
        if nums == None:
            print()
            break


a = genlist([1,2])
printlist(a)
so = Solution()
printlist(so.removeNthFromEnd(a, 2))

        
