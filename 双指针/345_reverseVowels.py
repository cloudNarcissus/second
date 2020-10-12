#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/9 19:36
# @Author : lantianyun l30001819
# @File : 345_reverseVowels.py

# 翻转字符串中的元音字母


class Solution:
    @classmethod
    def reverseVowels(self, s: str) -> str:

        str = list(s)
        head = 0
        tail = len(str)-1

        while head < tail:
            if str[head].lower() in ('a','e','i','o','u') and str[tail].lower() in ('a','e','i','o','u'):  # 注意坑：元音字符分大小写
                str[head],str[tail] = str[tail],str[head]
                head += 1
                tail -= 1
            elif str[head].lower() in ('a','e','i','o','u'):
                tail -= 1
            elif str[tail].lower() in ('a','e','i','o','u'):
                head += 1
            else:
                head += 1
                tail -= 1

        return ''.join(str)


print(Solution.reverseVowels("leetcode"))