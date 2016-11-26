# coding:UTF-8

'''
462. Minimum Moves to Equal Array Elements II
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
'''
'''
解题思路：
1. 计算数组的中位数
2. 排序
3. 奇数个数取中间数为 中位数
4. 偶数个数取中间两个数的平均数
'''

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        count = len(nums)

        if count%2 != 0:
            middleNum = nums[count/2]
        else:
            middleNum = (nums[count/2-1] + nums[count/2])/2

        totalSteps = 0
        for index in range(count):
            totalSteps += abs(middleNum - nums[index])

        return totalSteps


if __name__ == '__main__':
    solution = Solution()
    assert 0 == solution.minMoves2([1])
    assert 2 == solution.minMoves2([1,2,3])
    assert 11 == solution.minMoves2([1,12,2])