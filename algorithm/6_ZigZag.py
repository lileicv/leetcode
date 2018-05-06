#encoding=utf-8
'''
input: 
    str = 'abcdefghijk'
    nRows = 3
output:
    a   e   i
    b d f h j
    c   g   k
input:
    str = 'abcdefghijk'
    nRows = 4
output:
    a     g
    b   f h
    c e   i k
    d     j
'''

from math import ceil

def convert(s, numRows):
    if numRows == 1:
        return s
    ss = ['' for _ in range(numRows)]
    count = 0
    add = 1
    for i in range(len(s)):
        ss[count] += s[i]
        count += add
        if count == numRows:
            count -= 2
            add = -1
        elif count == -1:
            count = 1
            add = 1
    s = ''
    for i in range(numRows):
        s+=ss[i]
    return s

if __name__ == "__main__":
    rst = convert('PAYPALISHIRING', 1)
    print(rst)
