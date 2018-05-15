#encoding:utf-8

'''3Sum
输入一个数据，返回所有和为0的三元组

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

idea1:三级遍历：三个数由三个遍历得到
idea2:二级遍历：二个数遍历得到，第三个数用折半查找得到
上两种方式都会 time out
idea3:一级遍历：第一个数遍历获取，剩下的两个数查找得到
'''

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        threes = []
        lastnum = None
        for i in range(len(nums)):
            if nums[i] == lastnum:
                continue
            lastnum = nums[i]
            objvalue = -nums[i]
            low = i+1
            high = len(nums)-1
            while low < high:
                curvalue = nums[low]+nums[high]
                if curvalue==objvalue:
                    three = [nums[i], nums[low], nums[high]]
                    threes.append(three)
                    low += 1
                    while low<high and nums[low]==nums[low-1]:
                        low += 1
                    high -= 1
                    while low<high and nums[high]==nums[high+1]:
                        high -= 1

                elif curvalue>objvalue:
                    high -= 1
                elif curvalue<objvalue:
                    low += 1

        return threes

nums = [-2,0,1,1,2]
so = Solution()
print(so.threeSum(nums))