# -*- coding: utf-8 -*-
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        new_x = ''
        low = -2147483648   # 负2的31次方
        high = 2147483647   # 2的31次方减1
        if x == 0:
            return 0

        # 大于0的情况
        if x > 0:
            x = str(x)
            new_x = x[::-1]
            if x[-1] == '0':
                new_x = new_x[1::]

        # 小于0时
        if x < 0:
            x = str(x)
            x = x[1::]
            new_x = x[::-1]
            if x[-1] == '0':
                new_x = new_x[1::]
            new_x = '-' + new_x
        
        # 反转后不能溢出
        new_x = int(new_x)
        if new_x < low or new_x > high:
            return 0

        return int(new_x)
        