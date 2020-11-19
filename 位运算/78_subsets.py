#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/19 20:26
# @Author : lantianyun l30001819
# @File : 78_subsets.py

from typing import List

from itertools import combinations

def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []

    for i in range(len(nums) + 1):
        res.extend([list(x) for x in combinations(nums, i)])

    return res

