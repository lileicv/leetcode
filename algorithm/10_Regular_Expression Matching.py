'''
'.' -> Match any single character
'*' -> Match 0 or more of the preceding element

Input: str='aab' pattern='a*b'
Output: True

Input: str='ab' pattern='.*'
Output: True

Input: str='abcd' pattern='a*.'
Output：False

这个问题没有解出来，搜索了一下别人的方法，递归法，考虑每一种可能存在划分情况，然后把匹配结果或一下
这个方法的复杂度相当高
'''

class Solution():
    def isMatch(self, s, p):
        # pattern is empty
        if p=='':
            return not s 

        now_match = bool(s) and p[0] in [s[0], '.']

        if len(p)>=2 and p[1]=='*':
            return self.isMatch(s, p[2:]) or (now_match and self.isMatch(s[1:], p))
        else:
            return now_match and self.isMatch(s[1:], p[1:])

so = Solution()
# print(so.isMatch('abcd', 'a*b*c*d*'))
# print(so.isMatch('aa', 'a*'))
# print(so.isMatch('aa', 'a'))
# print(so.isMatch('aab', 'c*a*b'))
print(so.isMatch("","a*"))
