#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/19 19:36
# @Author : lantianyun l30001819
# @File : 136_singleNumber.py


# 只出现一次的数字 ，如 [4,1,2,1,2] 返回4.  注意要求复杂度为O(n)。且不用额外空间

# 知识：
# 0 ^ a = a
# a ^ b = b ^ a
# a ^ a = 0

# 因为是交换律，所以相同的数与或之后为0 ，然后剩下一个单数与0 与或后还是原数


def singleNumber(nums):
    a = 0
    for i in nums:
        a = a ^ i

    return a

print(singleNumber([4,1,2,1,2]))




from itertools import permutations, combinations

print()

l= []
l.e