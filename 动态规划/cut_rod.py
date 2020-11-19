#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/19 16:26
# @Author : lantianyun l30001819
# @File : cut_rod.py

import time
from common.cal_time import cal_time

# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40] # 该列表的下标对应钢管长度，其值对应钢管的价格
p = [0, 1, 1, 8, 9, 10, 17, 17, 20, 24, 30]


# 方法一：递归

from functools import lru_cache
@lru_cache()
def cut_rod_recursive(n):
    if n <= 1 :
        return p[n]
    else:
        max_ = p[n] # 不分的时候的价格

        for i in range(1,n):
            max_ = max(max_, p[i]+cut_rod_recursive(n-i))
        return max_

@cal_time
def cut_rod_recursive_time(n):
    print(cut_rod_recursive(n))

cut_rod_recursive_time(9)



# 方法二：动态规划

def cut_rod_dp(n):
    dp = []
    dp.append(p[0])
    for i in range(1,len(p)):
        max_ = p[i]  # 不切割
        for j in range(1,i):
            max_ = max(max_, dp[j] + dp[i-j])
        dp.append(max_)

    print(dp[n])

cut_rod_dp(3)





