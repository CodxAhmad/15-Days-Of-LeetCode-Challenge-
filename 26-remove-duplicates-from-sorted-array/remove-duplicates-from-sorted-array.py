class Solution(object):
    def removeDuplicates(self, nums):
        n = nums[0]
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != n:
                n = nums[i]
                nums[k] = n
                k += 1
        return k