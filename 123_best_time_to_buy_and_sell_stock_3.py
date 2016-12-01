# coding : UTF-8

'''
123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.
'''

class Solution(object):
    def maxProfit(self,prices):
        if len(prices) < 2:
            return 0

        oneTranProfit = []
        tempMaxProfit = 0
        curMin = prices[0]

        for i in range(len(prices)):
            tempMaxProfit = max(tempMaxProfit,prices[i] - curMin)
            oneTranProfit.append(tempMaxProfit)
            curMin = min(curMin,prices[i])

        maxProfit = 0
        tempMaxProfit = 0
        curMax = prices[len(prices)-1]
        for i in range(len(prices)-1,0,-1):
            tempMaxProfit = max( tempMaxProfit,curMax - prices[i])
            maxProfit = max(maxProfit,tempMaxProfit + oneTranProfit[i])
            curMax = max(curMax,prices[i])

        return maxProfit

if __name__ == '__main__':
    solution = Solution()
    assert 2 == solution.maxProfit([2,1,2,0,1])
