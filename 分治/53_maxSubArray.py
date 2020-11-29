#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/24 20:29
# @Author : lantianyun l30001819
# @File : 53_maxSubArray.py


class Solution:
    def maxSubArray(self, nums) -> int:

        total_max = nums[0]
        total_ = nums[0]
        for num in nums[1:]:
            total_ += num
            if total_ < num:
                total_ = num
            total_max = max(total_max, total_)

        return total_max


class Pushup:
    def __init__(self, lsum, rsum, msum, isum):
        self.lsum = lsum
        self.rsum = rsum
        self.msum = msum
        self.isum = isum

    def __add__(self, other):
        lsum = max(self.lsum, self.isum + other.lsum)
        rsum = max(other.rsum, other.isum + self.rsum)
        isum = self.isum + other.isum
        msum = max(self.msum, other.msum, self.rsum + other.lsum)
        return Pushup(lsum, rsum, msum, isum)


class Solution2:
    def maxSubArray(self, nums) -> int:
        pushup = self.f(nums)
        return pushup.msum

    def f(self, nums):
        if len(nums) == 1:
            return Pushup(nums[0],nums[0],nums[0],nums[0])

        mid = (len(nums)) // 2

        return self.f(nums[:mid]) + self.f(nums[mid:])


s2 = Solution2()
print(s2.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


