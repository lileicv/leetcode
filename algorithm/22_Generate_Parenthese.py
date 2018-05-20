''' Generate Parenthese
 For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

def run(m_l, m_r):
    '''
    : m_l number of (
    : m_r number of )
    : n   num of n
    '''
    print(m_l, m_r)
    if m_l==0 and m_r==1:
        return [')']

    elif m_l ==m_r:
        a = run(m_l-1, m_r)
        for i in range(len(a)):
            a[i] = '('+a[i]
        return a

    elif m_l==0:
        b = run(m_l, m_r-1)
        for i in range(len(b)):
            b[i] = ')' + b[i]
        return b
    else:
        a = run(m_l-1, m_r)
        for i in range(len(a)):
            a[i] = '(' + a[i]
        b = run(m_l, m_r-1)
        for i in range(len(b)):
            b[i] = ')' + b[i]
        return a + b


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return run(n,n)

so  = Solution()
print(so.generateParenthesis(3))