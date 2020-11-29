#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/19 20:26
# @Author : lantianyun l30001819
# @File : 78_subsets.py


# 找出所有子集。

from typing import List


# 方法一，直接调用库函数combinations，组合

from itertools import combinations,permutations

def subsets( nums: List[int]) -> List[List[int]]:
    res = []

    for i in range(len(nums) + 1):
        res.extend([list(x) for x in combinations(nums, i)])

    return res


L = [1,2,3]
print(subsets(L))



#