#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/16 9:09
# @Author : lantianyun l30001819
# @File : max_number.py

# 将数字按照字符串的方式拼接起来，可以拼接的最大的数字是

n = [7,778,76,79,63,1,311]


from functools import cmp_to_key

def max_number(n):
    m = list(map(str,n)) # 将每一个数字转成字符

    # 接下来把m中的元素按照字符顺序排序，但是要注意一种情况，就是两个串长度不一致且其中一个串是另一个串的子串，就不能简单得通过字符顺序来排
    # 这种情况下可以用两个串合并起来的实际数字来决定大小。也就是在用sort的时候，指定一个cmp函数，在3.6以后需要用 cmp_to_key实现

    def cmp_fun(x,y): # 定义一个自定义比较函数，两个数字一前一后，拼出来的谁大就是谁
        if x+y > y+x:
            return 1
        elif x+y < y+x:
            return -1
        else:
            return 0

    m.sort(key=cmp_to_key(cmp_fun),reverse=True)  # 在sort中应用这个自定义比较函数

    return ''.join(m)

print(max_number(n))