class Solution(object):
    def twoSum(self, nums, target):
        """
        数组中的某两个不同位置的数相加等于目标数
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    a.append(i)
                    a.append(j)
                    return a
        return a
        