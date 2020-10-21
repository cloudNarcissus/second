#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/20 20:22
# @Author : lantianyun l30001819
# @File : 198_rob.py

# 打家劫舍，要求偷盗的房间不能相邻。求最大金额
# 输入：nums = [1,2,3,1]
#               0 1 2 3

# f(4) = max(f(2)+nums[3], f(3))
# f(3) = max(f(1)+nums[2]), f(2))
# f(2) = max(f(0)+nums[1]), f(1))
# f(1) =

from typing import List
from functools import lru_cache

class Solution:
    @classmethod
    def rob(self, nums: List[int]) -> int:
        # 需要找到递推式。
        # 若偷第n间房子，则总金额就是n-2间房子的金额 + 第n间房子的金额, 即 f(n-2)+nums[n]
        # 若不偷第n间房子，则金额就等于n-1间房子的金额,即f(n-1)
        # 所以偷总数为n的房子的金额 = max( f(n-2)+nums[n], f(n-1) )
        @lru_cache()
        def f(n):
            if n == 0 : # 注意递归的终止条件
                return 0
            elif n == 1: # 注意递归的终止条件
                return nums[0]
            else:
                return max(f(n - 2) + nums[n-1],f(n - 1))

        if len(nums) == 0:
            return 0
        else:
            return f(len(nums))


print(Solution.rob([1,2,3,1]))

