#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/9 19:11
# @Author : lantianyun l30001819
# @File : 633_SumOfSquareNumbers.py

# 两数平方和


from math import sqrt,floor

class Solution:
    @classmethod
    def judgeSquareSum(cls, c: int) -> bool:
        head = 0
        tail = floor(sqrt(c))

        while head <= tail:
            if head ** 2 + tail ** 2 == c:
                return True
            elif head ** 2 + tail ** 2 > c:
                tail = tail-1
            elif head ** 2 + tail ** 2 < c:
                head = head+1
        else:
            return False

print(Solution.judgeSquareSum(85))