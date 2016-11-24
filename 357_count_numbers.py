class Solution(object):
    """docstring for problem 357.
       Given a non-negative integer n,count all numbers with unique digits,x,where 0<=x<10^n
    """
    def countNumbersWithUniqueDigits(self,n):
        if n > 10:
            return 0

        nums = [9]
        for x in range(9,0,-1):
            nums += nums[-1] * x,
        return sum(nums[0:n]) + 1

if __name__ == '__main__':
    solution = Solution()
    assert 10 == solution.countNumbersWithUniqueDigits(1)
    assert 91 == solution.countNumbersWithUniqueDigits(2)
    
