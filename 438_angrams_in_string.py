class Solution(object):
    """docstring for problem 436.
    Given a string s and a non-empty string p,find all the start indices of p's anagrams in s.
    String consists of lowercase English letters only and the length of both string s and p will not larger than 20,100.
    The order of output does not matter"""

    def findAnagrams(self,s,p):
        result = []
        if len(s) < len(p):
            return result

        dict= self.initDict(p)
        totalNum = len(p)

        left = 0
        right = 0

        while right < len(s):
            letter = s[right]
            right += 1
            if letter in dict:
                dict[letter] = dict[letter] - 1
                if dict[letter] >= 0:
                    totalNum -= 1
            else:
                dict = self.initDict(p)
                left = right
                totalNum = len(p)
                continue

            if totalNum == 0:
                result.append(left)

            if right - left == len(p):
                if s[left] in dict :
                    dict[s[left]] += 1
                    if dict[s[left]] > 0 :
                        totalNum += 1
                left += 1
        return result

    def initDict(self,str):
        dict = {}
        for left in xrange(len(str)):
            if str[left] not in dict:
                dict[str[left]] = 1
            else:
                dict[str[left]] += 1
        return dict

if __name__ == '__main__':
    solution = Solution()
    s = "cbaebabacd"
    p = "abc"

    print solution.findAnagrams(s,p)
