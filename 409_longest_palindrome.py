# coding: UTF-8

'''
409.Longest Palindrome
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

'''
解题思路：
1. 区分大小写
2. 统计每个字符出现的总数
'''

class Solution(object):
    def longestPalindrome(self,s):
        if s is None or len(s) == 0:
            return 0

        dict = {}

        for index in range(len(s)):
            if dict.has_key(s[index]):
                dict[s[index]] += 1
            else:
                dict[s[index]] = 1

        result = 0
        hasMid = False
        for key in dict.keys():
            if dict[key]%2 == 0:
                result += dict[key]
            else:
                result += (dict[key] -1)
                if not hasMid :
                    hasMid = True
                    result += 1

        return result

if __name__ == '__main__':
    solution = Solution()
    assert 0 == solution.longestPalindrome("")
    assert 7 == solution.longestPalindrome("abccccdd")
    assert 1 == solution.longestPalindrome("abc")
    assert 7 == solution.longestPalindrome("AAaaabbcd")