#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/21 14:05
# @Author : lantianyun l30001819
# @File : 213_rob2.py

# 核心原则就是：第一个和最后一个不能同时抢。 所以：要么不抢第一个，要么不抢最后一个。 注意，不抢第一个的时候，最后一个可抢可不抢；另一种情况同理 取两种情况中的最大值
from typing import List
from functools import lru_cache

class Solution:
    @classmethod
    def rob2(self, nums: List[int]) -> int:
        # 下面直接借用198的函数，计算无环的列表
        def rob(nums: List[int]) -> int:
            # 需要找到递推式。
            # 若偷第n间房子，则总金额就是n-2间房子的金额 + 第n间房子的金额, 即 f(n-2)+nums[n]
            # 若不偷第n间房子，则金额就等于n-1间房子的金额,即f(n-1)
            # 所以偷总数为n的房子的金额 = max( f(n-2)+nums[n], f(n-1) )
            @lru_cache()
            def f(n):
                # nonlocal best
                if n == 0:  # 注意递归的终止条件
                    return 0
                elif n == 1:  # 注意递归的终止条件
                    return nums[0]
                else:
                    x = f(n - 2) + nums[n - 1]
                    y = f(n - 1)
                    return max(x, y)

            if len(nums) == 0:
                return 0
            else:
                return f(len(nums))

        # 然后把原来的环打断成1:n  和 0:n-1 然后比较两者较大的。（也就是说0和n不能同时抢）
        if len(nums) == 0:  # 注意终止条件
            return 0
        elif len(nums) == 1:  # 注意终止条件
            return nums[0]
        else:
            return max(rob1(nums[1:]), rob1(nums[:len(nums) - 1]))


print(Solution.rob2([2,3,2]))
