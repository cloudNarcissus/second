#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/27 20:20
# @Author : lantianyun l30001819
# @File : 20_isValid.py


# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

class Solution:
    def __init__(self):
        self.d = [
            ('(',')'),
            ('{', '}'),
            ('[', ']')
        ]

    def isValid(self, s: str) -> bool:
        if s is None or s == "":
            return True

        l = list(s)
        stack = []
        for i in l:
            if not stack:
                stack.append(i)
            elif (stack[-1],i) in self.d:
                stack.pop()
            else:
                stack.append(i)

        if stack:
            return False
        else:
            return True

s = Solution()
print(s.isValid("()[]{}"))