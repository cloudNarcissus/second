#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/27 20:05
# @Author : lantianyun l30001819
# @File : 26_removeDuplicates.py

class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        max_ = max(nums)

        i = 0
        j = 0

        while nums[i] < max_:
            while nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]

        return i + 1

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))