#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/30 11:33
# @Author : lantianyun l30001819
# @File : 84_largestRectangleArea.py

# [2,1,5,6,2,3]
# 根据这个画矩形
from common.cal_time import cal_time

from typing import List
# 暴力1，对每一个可能的高度都遍历整个数组，找出对应的最长的长度
class Solution1:
    @cal_time
    def largestRectangleArea(self, heights: List[int]) -> int:

        levels = set(heights) # 取出不重复的高度
        s_max = 0

        for level in levels: # 对每一个可能的高度遍历
            level_len = 0
            level_len_max = 0
            for height in heights:
                if height >= level:  # 如果高度大于当前所求的高度，则长度+1
                    level_len += 1
                else:                # 否则长度又从0开始计数（保留之前遍历过的最大长度）
                    level_len_max = max(level_len_max, level_len)
                    level_len = 0
            else:
                level_len_max = max(level_len_max, level_len)
            s_max = max(s_max, level_len_max*level)
        return s_max



# 暴力2，以数组中的每一个数i为中心，向左和向右两个方向分别遍历，如果遇到第一个小于本值heights[i]的就停止遍历。从而求得当前值所能构成的矩形的最大面积
class Solution2:
    @cal_time
    def largestRectangleArea(self, heights: List[int]) -> int:

        s_max = 0
        len_ = len(heights)
        for i in range(len_):
            left = i - 1
            while left >=0 and heights[left] >= heights[i]:
                left -= 1
            right = i + 1
            while right < len_ and heights[right] >= heights[i]:
                right += 1
            s_max = max(s_max, (right - left - 1)*heights[i])
        return s_max
heights = []
s1 = Solution2()
s2 = Solution2()
print(s1.largestRectangleArea(heights))
print(s2.largestRectangleArea(heights))