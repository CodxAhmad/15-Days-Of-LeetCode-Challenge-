class Solution(object):
    def threeSum(self, nums):
        lis = []
        nums.sort()  
        for i in range(len(nums) - 2):  
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start, end = i + 1, len(nums) - 1  
            while start < end:
                current = nums[i] + nums[start] + nums[end]
                if current == 0:
                    lis.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif current > 0:  
                    end -= 1
                else:  
                    start += 1
        return lis