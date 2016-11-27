# coding : UTF-8

'''
423. Reconstruct Original Digits from English
Given a non-empty string contains an out-of-order English representation of digits 0-9,output the digits in ascending order
'''

import collections
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnts = collections.Counter(s)
        nums = ['six', 'zero', 'two', 'eight', 'seven', 'four', 'five', 'nine', 'one', 'three']
        numc = [collections.Counter(num) for num in nums]
        digits = [6, 0, 2, 8, 7, 4, 5, 9, 1, 3]
        ans = [0] * 10
        for idx, num in enumerate(nums):
            cntn = numc[idx]
            t = min(cnts[c] / cntn[c] for c in cntn)
            ans[digits[idx]] = t
            for c in cntn:
                cnts[c] -= t * cntn[c]
        return ''.join(str(i) * n for i, n in enumerate(ans))

if __name__ == '__main__':
    solution = Solution()
    #print solution.originalDigits('one')
    assert '11' == solution.originalDigits('oneone')
    assert '45' == solution.originalDigits('fviefuro')
    assert "0123456789" == solution.originalDigits("zeroonetwothreefourfivesixseveneightnine")