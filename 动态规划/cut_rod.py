#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/19 16:26
# @Author : lantianyun l30001819
# @File : cut_rod.py

import time
from common.cal_time import cal_time

# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40] # 该列表的下标对应钢管长度，其值对应钢管的价格
p = [0,1,10,8,9,10,17,17,20,24,30]



from functools import lru_cache
@lru_cache()
def cut_rod_recursive(n):
    if n <= 1 :
        print(())
        return p[n]
    else:
        max_ = p[n] # 不分的时候的价格
        cut = ()
        for i in range(1,n):
            if max_ < p[i]+cut_rod_recursive(n-i):
                cut  = (i, n - i)
                max_ = p[i]+cut_rod_recursive(n-i)
        print(cut)
        return max_

@cal_time
def cut_rod_recursive_time(n):
    print(cut_rod_recursive(n))

cut_rod_recursive_time(10)



# 如果用动态规划思想来做：
def cut_rod_dp(n):
    r = [0]
    for i in range(1,n+1):
        res = 0
        for j in range(1,i+1):
            res = max(p[i],p[j]+r[j])






