# coding: UTF-8
'''
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating,enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
'''

'''
问题点：
1. 忘记了负数的情况
'''

class Solution(object):
    def fractionToDecimal(self,numerator,denominator):
        results = []
        dict = {}

        # 处理分子或分母出现负数的情况
        if numerator * denominator < 0:
            results.append('-')

        if numerator < 0:
            numerator = abs(numerator)

        if denominator < 0:
            denominator = abs(denominator)

        while True:
            dict[numerator] = len(results)
            result = numerator/denominator
            results.append(str(result))
            new_numerator = numerator - denominator * result

            if new_numerator == 0:
                break

            # 判断是否需要添加小数点，这里判断条件依赖于前面的负数处理
            if new_numerator < denominator and not results.__contains__('.'):
                results.append('.')

            new_numerator *= 10

            if dict.has_key(new_numerator):
                start = dict[new_numerator]
                results.insert(start,'(')
                results.append(')')
                break

            numerator = new_numerator

        return ''.join(results)


if __name__ == '__main__':
    solution = Solution()
    assert '0.5' == solution.fractionToDecimal(1,2)
    assert '2' == solution.fractionToDecimal(2,1)
    assert '0.(6)' == solution.fractionToDecimal(2,3)
    assert '-6.25' == solution.fractionToDecimal(-50,8)