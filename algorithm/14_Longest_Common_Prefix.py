'''Find the longest common prefix

'flower', 'flow', 'flight' --> 'fl'
'dog', 'racecar', 'car' --> ''
'''

def commonStr(s1, s2):
    if len(s1)==0 or len(s2)==0:
        return ''
    max_str = ''
    k1 = 0
    k2 = 0
    s = ''
    while s1[k1]==s2[k2]:
        s += s1[k1]
        k1 += 1
        k2 += 1
        if k1 >= len(s1) or k2 >= len(s2):
            break
    if len(s) > len(max_str):
        max_str = s 
    return max_str

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        str1 = strs[0]
        for i in range(1,len(strs)):
            str1 = commonStr(str1, strs[i])
        return str1

so = Solution()
#print(so.longestCommonPrefix(["flower","flow","flight"]))
print(so.longestCommonPrefix(["dog","racecar","car"]))
