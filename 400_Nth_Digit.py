import math
class Solution(object):
    def findNthDigit(self,n):
        """
        :type n: int
        :rtype: int
        """
        number_per_digit = 1
        while n > 0:
            temp = n- number_per_digit * 9 * 10**(number_per_digit-1)
            if temp > 0:
                n = temp
                number_per_digit += 1
            else:
                break

        index = int(math.ceil(float(n)/number_per_digit))
        number = 10**(number_per_digit - 1) + index -1
        n -= number_per_digit * (index-1)
        return int(str(number)[n-1])

if __name__ == '__main__':
    solution = Solution()
    assert 3 == solution.findNthDigit(3)
    assert 1 == solution.findNthDigit(10)
    assert 0 == solution.findNthDigit(11)
    assert 5 == solution.findNthDigit(100)
    assert 7 == solution.findNthDigit(10000000)
