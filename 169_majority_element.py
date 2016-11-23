class Solution(object):
	"""docstring for problem 169."""
	def __init__(self, arg):
		super(Solution, self).__init__()
		self.arg = arg

	def majorityElement(arg,nums):
		dict = {}
		totalNum = len(nums)

		for index in xrange(totalNum):
			num = nums[index]
			if num in dict:
				dict[num] += 1
			else:
				dict[num] = 1

			if dict[num] >= totalNum/2:
				return num
		return 0
