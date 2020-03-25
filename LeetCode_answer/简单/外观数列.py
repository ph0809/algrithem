# -*- coding: utf-8 -*-
# -*- author: ph -*-
from itertools import groupby


class Solution(object):
    def countAndSay(self, n):
        result = '1'
        for i in range(1, n):
            result = ''.join([str(len(list(g))) + k for k, g in groupby(result)])
        return result


a = Solution()
print a.countAndSay(7)
