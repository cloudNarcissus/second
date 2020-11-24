#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/23 13:37
# @Author : lantianyun l30001819
# @File : 121_maxProfit.py

from typing import List

# 121 : 只能买卖一次。
class Solution121:
    def maxProfit(self, prices: List[int]) -> int:

        # 若昨天已经卖出，则最大利润就是昨天的 ，若今天卖出，就是今天的价格减去从历史到昨天以来的最低价
        # 因此公式为：dp[i] = max(dp[i-1], price[i]-minprice[i-1])

        if not prices:
            return 0

        dp = [0 for _ in range(len(prices))]

        minprice = prices[0]
        dp[0] = 0
        for i in range(1, len(prices)):
            minprice = min(minprice, prices[i - 1])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return max(dp)



# 122： 可以买卖多次
class Solution122:
    def maxProfit(self, prices: List[int]) -> int:

        # dp[i][1]表示今天持有股票的最大收益：
        #    情况1 : 昨天已卖，最大收益即为昨天的最大收益减去今天花费： dp[i-1][0] - price[i]
        #    情况2 : 昨天没卖，今天继续持有： dp[i-1][1]
        # dp[i][0]表示今天不持有股票的最大收益：
        #    情况1 : 昨天已经卖了，今天也不买，所以今天最大收益即为昨天的最大收益： dp[i-1][0]
        #    情况2 : 昨天没有卖，今天卖，所以今天最大收益为：dp[i-1][1] + price[i]

        if not prices:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(len(prices))]


        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])


        return max(dp[len(prices)-1])

    for i in enum
