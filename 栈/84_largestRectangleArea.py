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


# 方法3： 一个单调栈，这个方法不好

class Solution3:
    def __init__(self):
        self.stack = []
        self.s_max = 0

    @cal_time
    def largestRectangleArea(self, heights: List[int]) -> int:
        self.heights = heights
        self.max_list = [0 for i in self.heights]
        for i, height in enumerate(heights):
            # 入栈
            self.intoStack(i, height)

        # 最后如果栈里还有元素，就要依次出栈
        self.clearStack()
        print(self.max_list)
        return self.s_max

    def intoStack(self, i, height):
        if not self.stack or (self.stack and self.heights[self.stack[-1]] <= height): # 构造单调递增的栈
            self.stack.append(i)
        elif self.stack and self.heights[self.stack[-1]] > height: # 若遇到小的新值，就要出栈直到栈为空或者栈顶小于新值为止
            self.popStack(i, height)

    def popStack(self, i, height):
        while self.stack and self.heights[self.stack[-1]] > height:
            j = self.stack.pop()
            if self.stack:
                self.s_max = max(self.s_max, (i-j)*self.heights[j])
                self.max_list[j] = (i-j)*self.heights[j]
            else:
                self.s_max = max(self.s_max, i*self.heights[j])
                self.max_list[j] = i*self.heights[j]
        self.stack.append(i)

    def clearStack(self):
        max_index = len(self.heights)-1
        while self.stack:
            j = self.stack.pop()
            if self.stack:
                self.s_max = max(self.s_max, (max_index - self.stack[-1]) * self.heights[j])
                self.max_list[j] = (max_index - self.stack[-1]) * self.heights[j]
            else:
                self.s_max = max(self.s_max, (max_index + 1) * self.heights[j])
                self.max_list[j] = (j + 1) * self.heights[j]



# 方法4： 两个单调栈，分别从左和右遍历, 用栈获取暴利法中需要遍历才能得到的左右最小
class Solution4:
    def __init__(self):
        self.left_stack = []
        self.right_stack = []
        self.left_first_min = []
        self.right_first_min = []
        self.s_max = 0

    @cal_time
    def largestRectangleArea(self, heights: List[int]) -> int:
        self.heights = heights
        self.left_first_min = [0 for _ in self.heights]
        self.right_first_min = [0 for _ in self.heights]

        for i, height in enumerate(self.heights):
            self.intoStack(self.left_stack,self.left_first_min,i,height)

        for i in range(len(self.heights)-1,-1,-1):
            self.intoStack(self.right_stack,self.right_first_min,i,self.heights[i])

        for i, height in enumerate(self.heights):
            left_min = self.left_first_min[i]
            right_min = len(self.heights)  if self.right_first_min[i] == -1 else self.right_first_min[i]
            self.s_max = max(self.s_max, height*(right_min - left_min - 1))

        return self.s_max

        print(self.left_first_min)
        print(self.right_first_min)

    def intoStack(self,stack, min_list, i, height):
        if not stack:
            min_list[i]=-1
        elif stack and self.heights[stack[-1]] < height: # 构造单调递增的栈
            min_list[i]=stack[-1]
        elif stack and self.heights[stack[-1]] >= height: # 若遇到小的新值，就要出栈直到栈为空或者栈顶小于新值为止
            self.popStack(stack,min_list,i, height)
        stack.append(i)

    def popStack(self,stack,min_list,i, height):
        while stack and self.heights[stack[-1]] >= height:
            stack.pop()
        if stack:
            min_list[i]=stack[-1]
        else:
            min_list[i]=-1





heights = [1,1,4,4,1,1,1,1,1,1]
s4 = Solution4()
#print(s2.largestRectangleArea(heights))
print(s4.largestRectangleArea(heights))