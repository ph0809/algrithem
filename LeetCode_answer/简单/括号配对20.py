# -*- coding: utf-8 -*-
# -*- author: ph -*-


class Solution(object):
    def isValid(self, s):
        """
        判断输入的括号对是否匹配
        :param s:
        :return:
        """
        map_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        l = []
        for i in s:
            if map_dict.get(i) == None:
                l.append(i)
            elif len(l) == 0 or map_dict.get(i) != l[-1]:
                return False
            elif l[-1] == map_dict.get(i):
                l.pop()

        if len(l) == 0:
            return True
        else:
            return False

