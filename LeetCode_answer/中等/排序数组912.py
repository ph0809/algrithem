# -*- coding: utf-8 -*-
# -*- author: ph -*-

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        if length not in range(1, 50001):
            return []
        for i in range(length):
            if nums[i] not in range(-50000, 50001):
                return []
            for j in range(i + 1, length):
                if nums[j] < nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

        return nums


a = Solution()
print a.sortArray([5,2,3,1])