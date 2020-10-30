#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/30 10:17
# @Author : lantianyun l30001819
# @File : 215_nlargest.py

from typing import List

# 方法一： 排序
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

# 方法二： 堆
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify, nlargest
        #heapify(nums)
        return nlargest(k, nums)[-1]


