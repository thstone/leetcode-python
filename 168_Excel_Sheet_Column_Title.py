# coding=utf-8

'''
168.Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
'''

'''
解题思路：

实质是一个进制转换问题，整除要特殊考虑
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        titles = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = []

        while n > 0:
            index = n%26
            n /= 26
            if index == 0:
                result.append('Z')
                n -= 1
            else:
                result.append(titles[index - 1])

        result.reverse()
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()

    assert 'A' == solution.convertToTitle(1)
    assert 'AA' == solution.convertToTitle(27)
    assert 'AZ' == solution.convertToTitle(52)