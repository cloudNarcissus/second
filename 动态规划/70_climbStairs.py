#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/20 15:56
# @Author : lantianyun l30001819
# @File : 70_climbStairs.py

# 每次可以爬1或2阶台阶，有多少种不同方法
from functools import lru_cache

class Solution:
    @classmethod
    @lru_cache()
    def climbStairs(cls, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n > 2:
            return cls.climbStairs(n-1)+cls.climbStairs(n-2)

