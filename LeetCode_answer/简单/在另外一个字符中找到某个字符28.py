# -*- coding: utf-8 -*-
# -*- author: ph -*-


class Solution(object):
    def strStr(self, haystack, needle):
        """

        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:  # 找到第一个相等的位置
                if haystack[i:i+len(needle)] == needle:
                    return i

        return -1


a = Solution()
print a.strStr('flower', 'e')
