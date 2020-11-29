#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/25 17:06
# @Author : lantianyun l30001819
# @File : 真题_看山.py
#
# 某运营商在某山区做建网勘测，需要考虑山高对信号的影响。共有N座山在一条直线上，从左到右依次编号为1-N，山高数据存在数组height中。
# 勘测人员在编号为奇数的山头使用望远镜向左观测，在编号为偶数的山头使用望远镜向右观测，并记录在每个山头可以看到的山的数量。
# 请返回勘测人员所记录的看到的山的数量总和。
# 注意：根据视角的左右方向，在所观测的那一侧，后面矮的山或高度相同的山都会被前面高的山遮挡。
# 测试用例：
# 输入：height = [16,5,3,10,21,7]
# 输出：8


# 根据题意，数组若从0编号，则偶数向左看，奇数向右看。

# 方法就是用单调栈，然后从左往右遍历一次，再从右往左遍历一次
class Solution:
    def get_montain_cnt(self,height):

        # 先从左向右遍历，记录每个山头左边能看到的山头
        see_from_r_to_l = 0  # 从右向左看，左边第一个山头肯定为0
        stack = [height[0]] # 入栈
        for i in range(1,len(height)): # 从左向右遍历
            if i % 2 == 0:
                see_from_r_to_l += len(stack)
            self.stack_op(stack,height[i])

        see_from_l_to_r = 0
        stack = [height[-1]]
        for i in range(len(height)-2,-1,-1): # 从右向左遍历
            if i % 2 == 1:
                see_from_l_to_r += len(stack)
            self.stack_op(stack,height[i])

        return see_from_r_to_l+see_from_l_to_r

    def stack_op(self,stack, item):
        while stack and stack[-1] <= item:
            stack.pop()
        stack.append(item)

height = [16,5,3,10,21,7,2]
s = Solution()
print(s.get_montain_cnt(height))