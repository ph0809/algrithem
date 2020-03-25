# -*- coding: utf-8 -*-
# -*- author: ph -*-


class Solution(object):
    def searchInsert(self, nums, target):
        """
        二分查找的通用模板
        :param nums:  数组  int
        :param target:  int
        :return:
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] == target:
                pass    # 相关逻辑
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1

        return
