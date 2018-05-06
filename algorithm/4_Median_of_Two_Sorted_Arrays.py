#encoding:utf-8

'''
已知两个排序好的数组，返回两个数组的中值，举例：
[1,2],[3,4]  -> 2.5
[1,2],[10]   -> 2
[1,10],[2,4] -> 3
[1,5,9],[2,3,4] -> 3.5
'''
 

# 这么简单粗爆的方法，竟然通过测试了  ^v^!....
def findMedianSortedArrays(nums1, nums2):
    nums = nums1+nums2
    n = len(nums)
    # nums = sort(nums)
    nums.sort()
    if n%2==0:
        idx1 = int((n-1)/2)
        idx2 = idx1+1
    else:
        idx1 = (n-1)/2
        idx2 = idx1
    return (nums[idx1]+nums[idx2])/2

rst = findMedianSortedArrays([1,2],[3])
print(rst)


