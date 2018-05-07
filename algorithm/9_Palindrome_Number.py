#encoding:utf-8
'''
判断一个数字是不是回文
121 -> true
120 -> false
-12 -> false
'''

class Solution:
    def isPalindrome_1(self, x):
        if x<0:
            return False
        s = str(x)
        output = True 
        loopnum = int(len(s)/2)
        for i in range(loopnum):
            if s[i] != s[-i-1]:
                output = False
                break
        return output
    
    def isPalindrome(self, x):
        if x<0 or (x%10==0 and x!=0):
            return False
        y = 0
        
        while x>y:
            y = y*10 + x%10
            x //= 10

        return x==y or x==y//10


so = Solution()
print(so.isPalindrome_1(121))
print(so.isPalindrome(121))
