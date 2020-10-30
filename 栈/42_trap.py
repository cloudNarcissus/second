#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/28 20:25
# @Author : lantianyun l30001819
# @File : 42_trap.py

# 接雨水，输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]


height = [0,1,0,2,1,0,1,3,2,1,2,1]

from typing import List


# 方法1，暴力解法，即 每个坐标的储水量 = min(该坐标左边包含自身的最大值,该坐标右边包含自身的最大值)-自身值

class Solution1:
    def trap(self, height: List[int]) -> int:
        sum = 0
        for i in range(len(height)):
            diff = (min(max(height[:i+1]) if height[:i+1] else 0,max(height[i:]) if height[i:] else 0)-height[i])
            sum += diff*1

        return sum

s1 = Solution1()
print(s1.trap(height))


# 方法2， 上面每个坐标计算的时候都要扫描一遍左右最大。其实我们可以把这个值事先存起来，就不用重复扫描了

class Solution2:
    def trap(self, height: List[int]) -> int:

        # 先从左往右遍历
        max_left_list = []
        max_left = 0
        for i in range(len(height)):
            max_left = max(max_left,height[i])   # 节省时间的关键就在这里，这里用一个max暂存之前遍历到的max，从而在此基础上算，而不用像暴力法那样再次从头遍历
            max_left_list.append(max_left)
        # 再从右往左遍历
        max_right_list = [0 for _ in range(len(height))]  # 注意从右往左不能用append了，而是要对应下标
        max_right = 0
        for i in range(len(height)-1,-1,-1):
            max_right = max(max_right, height[i])
            max_right_list[i]=max_right


        # 然后再用暴力法里面那个公式，不同的是，这次不用计算max，而是直接取
        sum = 0
        for i in range(len(height)):
            diff = min(max_left_list[i],max_right_list[i]) - height[i]
            sum += diff * 1

        return sum

s2 = Solution2()
print(s2.trap(height))


# 方法3， 使用栈
# 这个栈是单调递减的，也就是说后入的元素的值比先入的小。
# 栈里面存的是数组的下标，这样可以计算长度差


class Solution3:
    def trap(self, height: List[int]) -> int:
        stack = []
        sum = 0
        for i in range(len(height)): # 外层循环遍历数组，并把每个元素入栈
            while stack and height[stack[-1]]<height[i]: # 只要栈顶的元素小于当前遍历的数组的元素，就说明出现了水洼。就可以进入累加流程
                floor = stack.pop() # 先弹出当前的栈顶，作为洼地，因此取名为floor
                if stack: # 避免出现弹出以后栈为空，下面的stack[-1]就会报错
                    sum += (min(height[i],height[stack[-1]])-height[floor])*(i-stack[-1]-1) # 高*长

            else: # 否则就是继续维持单调递减的栈，将新的元素入栈
                stack.append(i)
        return sum

height = [4,2,0,3,2,5]
s3 = Solution3()
print(s3.trap(height))



# 方法4， 使用双指针






