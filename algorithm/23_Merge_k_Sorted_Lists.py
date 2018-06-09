'''
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def genlist(nums):
    if nums == []:
        return None
    li = ListNode(nums[0])
    pt = li
    for i in nums[1:]:
        pt.next = ListNode(i)
        pt = pt.next
    return li

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        lists_ = []

        for li in lists:
            if li == None:
                continue
            while True:
                lists_.append(li.val)
                if li.next == None:
                    break
                li = li.next
        lists_.sort()
        return genlist(lists_)


a = genlist([1,4,5])
b = genlist([1,3,4])
c = genlist([2,6])

so = Solution()
d = so.mergeKLists([a,b,c])
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
printlist(d)