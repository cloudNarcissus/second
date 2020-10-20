#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/19 10:51
# @Author : lantianyun l30001819
# @File : fibnacci.py

def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n-1) + fibnacci(n-2)

# 用递归方式计算的时候，不会缓存中间结果，导致每个f(n)都会计算多次因此效率很低，（即子问题的重复计算）
print(fibnacci(100))

# 使用lru_cache缓存中间结果，改善了这种情况
from functools import lru_cache
@lru_cache()
def fibnacci_cache(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci_cache(n-1) + fibnacci_cache(n-2)

print(fibnacci_cache(100))


# 当然，我们可以不用递归来实现，也就是动态规划（DP）的思想。也就是先找出递推式


