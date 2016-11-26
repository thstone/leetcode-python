# coding: UTF-8

'''
179. Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

'''

'''

class Solution(object):
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = sorted(map(str,nums),lambda x,y: cmp(y + x,x + y))
        result = ''.join(nums).lstrip('0')
        return result or '0'

    # 第二版，思路简单，效率提高，还不是很理想
    def CompareTwoInteger(self,value1,value2):
        return cmp(str(value1) + str(value2), str(value2)+str(value1))

    # 第一版  执行效率低，
    def CompareTwoInteger_old(self,value1,value2):
        '''
        :param value1:
        :param value2:
        :return:
        '''
        if value1 == value2:
            return 0

        list1 = self.CovertIntegerToList(value1)
        list2 = self.CovertIntegerToList(value2)
        len1 = len(list1)
        len2 = len(list2)

        index1 = 0
        index2 = 0
        max_num = len1 *len2

        while (index1 < len1 or index2 < len2) and max_num > 0:
            max_num -= 1

            if list1[index1] > list2[index2]:
                return 1

            if list1[index1] < list2[index2]:
                return -1

            index1 = (index1 + 1)%len1
            index2 = (index2 + 1)%len2

        return 0

    def CovertIntegerToList(self,integer):
        count = len(str(integer))
        value_list = []
        while count > 0:
            count -= 1
            first_number = integer/10**(count)
            value_list.append(first_number)
            integer -= first_number * 10**count
        return value_list


if __name__ == '__main__':
    solution = Solution()
    assert '0' == solution.largestNumber([0,0])
    assert '12121' == solution.largestNumber([121,12])
    assert '9534330' == solution.largestNumber([3, 30, 34, 5, 9])