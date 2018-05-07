'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''

'''
左右两个指针，依次移动小值对应的指针
'''

class Solution:
    def maxArea(self, height):
        '''
        type height: List[int]
        rtype: int
        '''

        n = len(height)
        maxv = 0
        l = 0
        r = len(height)-1
        while l<r:
            v = min(height[l],height[r])*(r-l)
            maxv = max(maxv, v)
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
                
        return maxv


import time
time1 = time.clock()
so = Solution()
a = [2,3,4,5,18,17,6]
print(so.maxArea(a))
print(time.clock()-time1)