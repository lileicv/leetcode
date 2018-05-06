#encoding:utf-8

'''
判断最大的回文串（一个即可）

abcba,deeed,abba 这类的左右对称字符串称为回文

本程序 1032ms，leetcode 上还有一波更快的程序，二刷的时候注意提升一下
'''

# 发现局部最长的回文串
def localLongestPalindrome(s, idx1, idx2):
    if s[idx1]!=s[idx2]:
        return s[idx1]
    n = len(s)
    while True:
        p1 = idx1 - 1
        p2 = idx2 + 1
        if p1 < 0 or p2 == n:
            return s[idx1:idx2+1]
        if s[p1]==s[p2]:
            idx1 -= 1
            idx2 += 1
        else:
            return s[idx1:idx2+1]


def longestPalindrome(s):
    n = len(s)
    max_str = ''
    for i in range(n):
        rst = localLongestPalindrome(s, i, i)
        if len(max_str)<len(rst):
            max_str = rst
    for i in range(n-1):
        rst = localLongestPalindrome(s, i, i+1)
        if len(max_str)<len(rst):
            max_str = rst
    return max_str

if __name__ == "__main__":
    rst = localLongestPalindrome('1223', 1,2)
    print(rst)

    rst = longestPalindrome('1223225445')
    print(rst)
