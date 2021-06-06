#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   problem_627.py
@Time    :   2021/06/04 20:38:36
@Author  :   yanxinyi
@Version :   v1.0
@Contact :   yanxinyi620@163.com
@Desc    :   None
'''

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        # s = 'abccccdd'
        s_list = list(s)
        s_uniq = set(s_list)

        s_dict = {}
        for key in s_uniq:
            key_num = len([i for i in s_list if i == key])
            s_dict[key] = key_num
        
        s_long = len(s_list)
        for i in s_dict.values():
            if i%2 != 0:
                s_long -= 1

        if s_long < len(s_list):
            s_long += 1

        print(s_long)
        return s_long


if __name__=="__main__":
    r = Solution()
    s_long = r.longestPalindrome('abccccdd')
    print(s_long)

