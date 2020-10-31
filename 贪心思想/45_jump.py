#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/31 16:19
# @Author : lantianyun l30001819
# @File : 45_jump.py

# 输入: [2,3,1,1,4]   每个数字代表在该位置能够跳跃的最大步数。假设你总是可以到达数组的最后一个位置。
nums = [2,3,1,1,4]

# 思路1，用动态规划，要跳到最后一个位置，那么问题变为跳到最后一个位置的前一个位置。于是找出哪些点能够一步跳到最后的位置：
# 设点的位置为i，终点的位置为n，则 nums[i]  >= n-i 即可

from typing import List

from functools import lru_cache

class Solution1:
    def jump(self, nums: List[int]) -> int:

        @lru_cache()
        def findstep(n): #这里n是数组的最大下标，也就是len-1
            if n <= 0:
                return 0
            laststep  = [i for i in range(n) if nums[i] >= n-i]
            if laststep:
                # 对可到达的每个坐标分别计算，然后求最小
                return min(map(findstep,laststep))+1
            else: # 这个分支不会执行，因为条件中说：假设你总是可以到达数组的最后一个位置。所以laststep不会为空
                return None

        return findstep(len(nums)-1)

s = Solution1()
print(s.jump(nums))


class Solution2:
    def jump(self, nums: List[int]) -> int:

        @lru_cache()
        def findstep(n): #这里n是数组的最大下标，也就是len-1
            if n <= 0:
                return 0
            for i in range(n):
                if nums[i] >= n - i:
                    return findstep(i)+1

        return findstep(len(nums)-1)

s = Solution2()
print(s.jump(nums))



# 上面两种逆向的贪心都会超时。下面正向贪心
# 思路就是从1开始，查看能够跳跃到哪里，然后选择最远的那个。

class Solution2:
    def jump(self, nums: List[int]) -> int:
        step = 0
        for i in range(len(nums)-1):
            for
            maxpoint = max([nums[i+j] for j in range(1,nums[i+1])])



s = Solution2()
print(s.jump(nums))














