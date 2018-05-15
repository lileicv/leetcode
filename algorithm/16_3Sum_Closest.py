#encoding:utf-8

'''3Sum_Closest
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = sum(nums[0:3])
        mindist = abs(closest-target)
        #print(closest)

        nums.sort()
        lastnum = None
        for i in range(len(nums)):
            if nums[i] == lastnum:
                continue
            lastnum = nums[i]

            low = i+1
            high = len(nums)-1
            while low < high:
                close = nums[i]+nums[low]+nums[high]
                dist = close - target
                if abs(dist)<mindist:
                    mindist = abs(dist)
                    closest = nums[i]+nums[low]+nums[high]
                    #print(nums[i], nums[low], nums[high], mindist)
                if dist == 0:
                    return close
                elif dist>0:
                    high -= 1
                elif dist<0:
                    low += 1

        return closest

nums = [0,1,2]
target = 3
so = Solution()
print(so.threeSumClosest(nums, target))