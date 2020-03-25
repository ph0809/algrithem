# -*- coding: utf-8 -*-
# -*- author: ph -*-


class Solution(object):
    def removeElement(self, nums, val):
        """
        采用逆序遍历不会影响到前面没有比较过的数，如果是正序的话，则每次pop之后后面的数会自动移到前面来
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = len(nums)

        for i in range(count-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)

a = Solution()
print a.removeElement([3,2,2,3], 3)