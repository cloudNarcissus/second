#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/16 19:44
# @Author : lantianyun l30001819
# @File : 455_findContentChildren.py

# 输入: g = [1,2,3], s = [1,1]    g是小朋友的胃口   s是饼干    要让尽可能多的小朋友满足
# # 输出: 1

from typing import List

class Solution:
    @classmethod
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() # 需求按照从小到大排序
        s.sort() # 供给按照从小到大排序

        i = 0 #
        j = 0

        while i < len(g):
            if j >= len(s):
                break
            if g[i] <= s[j]:
                i += 1
            j += 1

        return i

print(Solution.findContentChildren(g = [1,2], s = [1,2,3]))