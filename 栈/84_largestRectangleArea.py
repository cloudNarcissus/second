#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/30 16:48
# @Author : lantianyun l30001819
# @File : 84_largestRectangleArea.py


# [2,1,5,6,2,3]
# 根据这个画矩形
from common.cal_time import cal_time

from typing import List
# 注：暴力1在《哈希表》这个文件夹内
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

# 方法3： 单调栈

class Solution2:
    def __init__(self):
        self.stack = []
        self.s_max = 0

    @cal_time
    def largestRectangleArea(self, heights: List[int]) -> int:
        self.heights = heights
        for i, height in enumerate(heights):

            # 入栈
            self.intoStack(i, height)

    def intoStack(self, i, height):
        if not self.stack or (self.stack and self.stack[-1] <= height): # 构造单调递增的栈
            self.stack.append(i)
        elif self.stack and self.stack[-1] > height: # 若遇到小的新值，就要出栈直到栈为空或者栈顶小于新值为止
            self.popStack(i, height)

    def popStack(self, i, height):
        while self.stack and self.stack[-1] > height:
            j = self.stack.pop()
            if self.stack:
                self.s_max = max(self.s_max, (i-j)*self.heights[j])
            else:
                self.s_max = max(self.s_max, i*self.heights[j])
        self.stack.append(i)


