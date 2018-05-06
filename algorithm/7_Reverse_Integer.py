'''
Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21
'''

class Solution:
    def reverse(self, x):
        # overflow return 0
        # get the sign
        if x<0:
            flag = -1
        else:
            flag = 1
        # reverse
        x = abs(x)
        intstr = ''
        while True:
            ge = x % 10
            x = x // 10
            intstr += str(ge)
            if x==0:
                break
        if flag == -1:
            intstr = "-"+intstr
        x = int(intstr)
        if x<-2**31 or x>2**31-1:
            return 0
        else:
            return int(intstr)

solution = Solution()
rst = solution.reverse(1534236469)
print(rst)

