#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/9 20:23
# @Author : lantianyun l30001819
# @File : 680_validPalindrome.py

# 验证回文字串（可以至多删除一个字符）

class Solution:

    # 先编写一个函数判断一个子串在不删除字符的情况下是否是回文
    @classmethod
    def isPalindrome(self, L) -> bool:
        head = 0
        tail = len(L) - 1
        while head < tail:
            if L[head] == L[tail]:
                head += 1
                tail -= 1
            else:
                return False
        return True

    # 然后在可以删除一个字符的情况下，判断删除后子串是否是回文
    @classmethod
    def validPalindrome(self, s: str) -> bool:
        str = list(s)
        head = 0
        tail = len(str)-1
        while head <= tail:
            if str[head] == str[tail]:
                head += 1
                tail -= 1
            elif str[head] != str[tail]: #遇到不相同的字符，可以删除左边，也可以删除右边
                return self.isPalindrome(str[head+1:tail+1]) or self.isPalindrome(str[head:tail])
        return True


print(Solution.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))



import random
li = [i for i in range(1,10000)]
random.shuffle(li)
print(li)


print(len('only_allow_merge_if_all_discussions_are_resolved'))