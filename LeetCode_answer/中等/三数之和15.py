# -*- coding: utf-8 -*-
# -*- author: ph -*-


class Solution(object):
    def threesum(self, nums):
        """
        数组中的三个元素和为0
        :param nums: 包含n个整数的数组
        :return: 元素为三元组的数组
        """
        # three_sum_set = []
        # three_sum = []
        #
        # if nums is None:
        #     return three_sum_set
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 three_sum = [nums[i], nums[j], nums[k]]
        #                 three_sum.sort()
        #                 if three_sum in three_sum_set:
        #                     continue
        #                 else:
        #                     three_sum_set.append(three_sum)
        #                 # continue
        #
        # three_sum_set = three_sum_set.sort(key=lambda i: i in three_sum_set)
        # return three_sum_set

        # if len(nums) < 3:
        #     return []
        # '''先对数组排序, 遍历数组遇到与前一个元素相同的情况可直接跳过'''
        # nums.sort()
        # target_hash = {-x: i for i, x in enumerate(nums)}
        # res = []
        # res_hash = {}
        # for i, first in enumerate(nums):
        #     '''当前元素与前一个元素相同时, 可直接跳过以优化性能'''
        #     if i > 0 and first == nums[i - 1]:
        #         continue
        #     for j, second in enumerate(nums[i + 1:]):
        #         '''检查两数之和是否存在于哈希表中'''
        #         if first + second in target_hash:
        #             target_index = target_hash[first + second]
        #             if target_index == i or target_index == i + j + 1:
        #                 continue
        #             '''将找到的结果存入另一个哈希表中, 避免包含重复结果'''
        #             row = sorted([first, second, nums[target_index]])
        #             key = ",".join([str(x) for x in row])
        #             if key not in res_hash:
        #                 res.append(row)
        #                 res_hash[key] = True
        # return res

        l = len(nums)
        if not nums or l < 3:
            return []
        nums.sort()  # python的sort用的是timesort算法，具体如下
        res = []
        for i in range(l):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 跳出本次循环
            left = i + 1
            right = l - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # 这里跟下面的边界比较是用来防止越界的，所以不能省！！！
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


a = Solution()
print a.threesum([-1, 0, 1, 2, -1, -4])

