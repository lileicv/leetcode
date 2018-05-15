'''Letter Combinations of Phone Number
1       2(abc)  3(def)
4(ghi)  5(jkl)  6(mno)
7(pqrs) 8(tuv)  9(wxyz)
*       0       #

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=='':
            return []
        t = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        o = ['']
        for i in digits:
            c = t[i]
            o1 = []
            for j in c:
                for k in o:
                    o1.append(k+j)
            o = o1
        return o

so = Solution()
print(so.letterCombinations('23'))

