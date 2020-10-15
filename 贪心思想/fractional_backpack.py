#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/15 20:07
# @Author : lantianyun l30001819
# @File : fractional_backpack.py

# 背包问题
goods = [(60,10),(100,20),(120,30)] # 每个商品元组表示(价格，重量)

def fractional_backpack(goods,w):
    goods.sort(key=lambda x:x[0]/x[1],reverse=True) # 按照单价从大到小排序

