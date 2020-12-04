#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/3 11:43
# @Author : lantianyun l30001819
# @File : 704_1203.py

class Solution:
    def search(self, nums, target: int) -> int:

        import bisect
        res = bisect.bisect_left(nums , target)
        if res < len(nums) and nums[res] == target:
            return res
        else :
            return -1