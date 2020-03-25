# -*- coding: utf-8 -*-
# -*- author: ph -*-


class Solution(object):
    def searchInsert(self, nums, target):
        """
        搜索插入位置，如果没有这个数，则返回适合的插入位置
        :param nums:
        :param target:
        :return:
        """
        nums.sort()   # 先排序
        if max(nums) < target:
            return len(nums)
        if min(nums) > target:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] < target:
                    continue
                return i
