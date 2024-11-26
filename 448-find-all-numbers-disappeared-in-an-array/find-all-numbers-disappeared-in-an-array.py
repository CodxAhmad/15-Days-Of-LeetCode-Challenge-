class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums_set = set(nums)
        x = len(nums)
        lis = []
        for i in range(1, x + 1):
            if i not in nums_set:
                lis.append(i)
        return lis