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


nums = [1, 2, 3, 4, 5]
k = 3


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import nlargest
        return nlargest(k, nums, key=lambda x: -1 * x)


s = Solution2()
print(s.findKthLargest(nums, k))
