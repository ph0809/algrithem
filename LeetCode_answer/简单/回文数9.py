class Solution(object):
    def isPalindrome(self, x):
        """
        回文数：正过来和反过来的数一样
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        new_x = x[::-1]
        if x == new_x:
            return True
        return False
