#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/31 9:47
# @Author : lantianyun l30001819
# @File : 122_maxProfit.py


# 输入: [7,1,5,3,6,4]  求最大的股票交易收益

# 因为可以当天卖了前一天的再买入当天的，所以可以把问题简化为只看邻近的两天。因此，只要后一天比前一天高，那么前一天就买入，后一天就卖出

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:
            return  0
        sum = 0
        for i in range(1,len(prices)):  # 遍历从第二天开始，然后每天与昨天比较，如果比昨天大，那么就累加今天和昨天的差值
            if prices[i] > prices[i-1]:
                sum += prices[i]-prices[i-1]
        return sum



