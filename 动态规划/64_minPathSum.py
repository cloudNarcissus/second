#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/21 19:34
# @Author : lantianyun l30001819
# @File : 64_minPathSum.py

from typing import List

class Solution:
    @classmethod
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)   # m行   这里千万要注意，如果m == 0的时候，grid[0]会报错，所以判断m==0要在取n=len(grid[0])之前。
        if m == 0:
            return 0

        n = len(grid[0]) # n列
        if  n == 0:
            return 0

        res = [[0 for _ in range(n)] for _ in range(m)] # 定义跟问题同规模的grid。用于动态规划
        res[0][0] = grid[0][0]

        for j in range(1,n): # 初始化第一行
            res[0][j] = res[0][j-1]+grid[0][j]
        for i in range(1,m):    # 初始化第一列
            res[i][0] = res[i-1][0]+grid[i][0]

        # 然后从第二行第二列开始，应用递推公式： res[i][j] = min(res[i-1][j],res[i][j-1])
        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = min(res[i-1][j],res[i][j-1]) + grid[i][j]

        return res[m-1][n-1]


grid =[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(Solution.minPathSum(grid))