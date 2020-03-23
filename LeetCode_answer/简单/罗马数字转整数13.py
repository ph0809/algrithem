class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping_list_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }      
        ans=0        
        for i in range(len(s)):            
            if i<len(s)-1 and mapping_list_dict[s[i]]<mapping_list_dict[s[i+1]]:     
                ans-=mapping_list_dict[s[i]]
            else:
                ans+=mapping_list_dict[s[i]]
        return ans