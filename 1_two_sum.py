class Solution(object):
    """docstring for problem 1."""
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

    def twoSum(self,nums,target):
        dict = {}
        for index in xrange(len(nums)):
            value = nums[index]
            if target - value in dict:
                return (dict[target - value],index)
            dict[value] = index


if __name__ == '__main__':
    solution = Solution
    solution.twoSum([1,2],3)
