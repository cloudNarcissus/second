#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/6 15:21
# @Author : lantianyun l30001819
# @File : 679_judgePoint24.py

# 四个数字通过加减乘除组成24点

# 思路就是四个数字中随机选两个，这俩通过加减乘除得到一个数，然后用结果替代原来的两个数，就变成了三个数字的24点，规模就缩小了
# 三个数字中又随机选两个，
# 。。。最后剩一个数字，判断其与10^-6的误差。

from typing import List

DEVIATION = 1e-6        # 误差是10的-6次方，即10**-6


class Solution:
    @classmethod
    def judgePoint24(self, nums: List[int]) -> bool:

        lenth = len(nums)
        if lenth == 1:
            return abs(nums[0] - 24) < DEVIATION

        is_valid = False
        for i in range(lenth):
            for j in range(i+1, lenth):
                # 复制列表，用切片浅拷贝即可
                new_nums = nums[:]
                # 取出两个数,先取j，因为j在后，不影响i的索引
                number_j = new_nums.pop(j)
                number_i = new_nums.pop(i)

                # 两个数经过计算，与new_nums合并成一个新的列表; 加法和乘法只有一种形式，减法有两种，除法要判断除数不为0
                is_valid = is_valid or\
                           self.judgePoint24(new_nums + [number_j+number_i])
                is_valid = is_valid or\
                           self.judgePoint24(new_nums + [number_i * number_j])
                is_valid = is_valid or \
                           self.judgePoint24(new_nums + [number_j - number_i])
                is_valid = is_valid or \
                           self.judgePoint24(new_nums + [number_i - number_j])
                if number_j:
                    is_valid = is_valid or self.judgePoint24(new_nums + [number_i / number_j])
                if number_i:
                    is_valid = is_valid or self.judgePoint24(new_nums + [number_j / number_i])

        return is_valid

print(Solution.judgePoint24([1, 2, 3, 4]))