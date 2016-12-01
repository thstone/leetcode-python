class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        maxProfit = 0
        curMin = prices[0]

        for i in range(len(prices)):
            maxProfit = max(maxProfit,prices[i] - curMin)
            curMin = min(curMin,prices[i])

        return maxProfit

if __name__ == '__main__':
    solution = Solution()
    assert 1 == solution.maxProfit([7,6,4,3,1,2])