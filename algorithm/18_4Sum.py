'''3Sum

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        out = []
        lasti = None
        for i in range(len(nums)-3):
            if lasti == nums[i]:
                continue
            lasti = nums[i]
            lastj = None
            for j in range(i+1,len(nums)-2):
                if nums[j] == lastj:
                    continue
                lastj = nums[j]
                low = j+1
                high = len(nums)-1
                new_target = target - nums[i] - nums[j]
                while low<high:
                    cur = nums[low] + nums[high]
                    if cur ==  new_target:
                        temp = [nums[i], nums[j], nums[low], nums[high]]
                        out.append(temp)
                        low += 1
                        while low<high and nums[low]==nums[low-1]:
                            low += 1
                        high -= 1
                        while low<high and nums[high]==nums[high+1]:
                            high -= 1
                    elif cur > new_target:
                        high -= 1
                    else:
                        low += 1
        return out

so = Solution()
print(so.fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9))