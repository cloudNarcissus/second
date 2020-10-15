#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/15 19:20
# @Author : lantianyun l30001819
# @File : change_money.py

# 找钱，使得找钱的总张数最少

t =  [100,50,20,5,1]  # 钱币面额，假设已经倒序排好
def change(t,n): # n表示总额
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):  # enumerate用于给一个可迭代对象生成序列号
        m[i] = n // money   # 整除，即取商
        n = n % money         # 取余数
    return m,n

print(change(t,377))