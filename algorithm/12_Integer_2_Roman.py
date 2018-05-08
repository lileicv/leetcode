'''
Convert number 2 roman 


Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

intToRoman(3) = III
intToRoman(4) = IV
intToRoman(8) = VIII
intToRoman(1994) = MCMXCIV
'''

class Solution:
    def intToRoman_1(self, num):
        """
        :type num: int
        :rtype: str
        """
        t1 = ['', 'a','aa','aaa','ab','b','ba','baa','baaa','ac']
        t2 = ['I','V','X','L','C','D','M', ' ', ' ']
        nums = []
        while num>0:
            nums.append(num%10)
            num //= 10
        #print(nums)
        obj = ''
        for i in range(len(nums)):
            s1,s2,s3 = t2[2*i:2*i+3]
            temp = t1[nums[i]]
            obj = temp.replace('a',s1).replace('b',s2).replace('c',s3) + obj
            #print(s1,s2,s3, obj)
        return obj

    def intToRoman(self, num):
        """
        : 第二种方法，查表法
        :type num: int
        :rtype: str
        """
        t = [['','I','II','III','IV','V','VI','VII','VIII','IX'],
              ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
              ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
              ['','M','MM','MMM']]
        nums = []
        while num>0:
            nums.append(num%10)
            num //= 10
        #print(nums)
        obj = ''
        for i in range(len(nums)):
            obj = t[i][nums[i]] + obj
            #print(s1,s2,s3, obj)
        return obj


so = Solution()
print(so.intToRoman(1994))

