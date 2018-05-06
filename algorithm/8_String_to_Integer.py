#encoding:utf-8
'''
提取字符串中的数字，如果开始字符串空格，向后遍历直到发现数字
如果开始字符串字母，解码失败，返回0
如果超出范围，返回 2^31-1 或 -2^31

Input: "42"
Output: 42

Input: "   -42"
Output: -42

Input: "4193 with words"
Output: 4193

Input: "words and 987"
Output: 0

Input: "-91283472332"
Output: -2147483648
'''

class Solution:
    def myAtoi(self, str):
        objstr = ""
        sign = 1
        findnum = False
        for i in range(len(str)):
            if findnum:
                if not str[i].isdigit():
                    break
                else:
                    objstr += str[i]
            else:
                if str[i] == " ":
                    continue
                elif str[i].isdigit():
                    objstr += str[i]
                    findnum = True
                    
                elif str[i] in ['-', '+']:
                	if i != len(str)-1:
                		if str[i+1].isdigit():
                			if str[i]=='-':
                				sign = -1
                		else:
                			break 
                else:
                    break

        if objstr == "":
            output = 0
        else:
            output = sign*int(objstr)
        if output > 2**31-1:
            output = 2**31-1
        elif output< -2**31:
            output = -2**31
        return output

solu = Solution()
print(solu.myAtoi("+1"))


