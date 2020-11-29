#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/10 9:08
# @Author : lantianyun l30001819
# @File : 704_search.py

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        import bisect
        if target in nums:
            return bisect.bisect_left(nums , target)
        else :
            return -1

class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        else:
            return -1