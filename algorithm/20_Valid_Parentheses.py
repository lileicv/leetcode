'''
()   --> true
{}[] --> true
{]   --> false
{[]} --> true
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            elif i == ')':
                if len(stack)!=0 and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False
            elif i == ']':
                if len(stack)!=0 and stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False
            elif i =='}':
                if len(stack)!=0 and stack[-1]=='{':
                    stack.pop(-1)
                else:
                    return False
        if len(stack)!=0:
            return False
        return True

s = '['
so = Solution()
print(so.isValid(s))