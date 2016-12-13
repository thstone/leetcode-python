# coding=utf-8

'''
191. Number of 1 Bits
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''

'''
解题思路：
1. 十进制转换成二进制 ：bin()函数
2. 统计字符串中出现某子字符串的次数 ：string.count(sub,begin,end)
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

if __name__ == '__main__':
    solution = Solution()
    assert 0 == solution.hammingWeight(0)
    assert 3 == solution.hammingWeight(11)