class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # str_min = min(strs)
        # str_max = max(strs)
        # for i, x in enumerate(str_min):
        #     if x!=str_max[i]:
        #         return str_max[:i]
        # return str_min

        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res += x[0]
        return res




