'''Convert Roman 2 integer

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

III --> 3
LVIII --> 58
MCMXCIV --> 1994
'''

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {'I':1,"V":5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n = len(s)
        value = 0
        for i in range(len(s)):
            #print(s[i])
            if i+1 < len(s):
                if table[s[i]] < table[s[i+1]]:
                    value -= table[s[i]]
                    #print('a')
                else:
                    value += table[s[i]]
                    #print('b')
            else:
                value += table[s[i]]
                #print('c')
        return value

so = Solution()
print(so.romanToInt('MCMXCIV'))
