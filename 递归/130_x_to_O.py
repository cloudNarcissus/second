#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/6 19:37
# @Author : lantianyun l30001819
# @File : 130_x_to_O.py

from functools import lru_cache

from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None

        x_size = len(board)
        if x_size <= 1:
            return board
        y_size = len(board[0])
        if x_size <= 1:
            return board

        def dfs(x, y):
            # 深度遍历的退出条件：超出矩阵边界或者值不为O
            if not 0 <= x < x_size or not 0 <= y < y_size or board[x][y] != 'O':
                return

            # 遍历之后设置值为-，表示没有被包围，因为参与深度遍历的起始节点就是边界上的O
            board[x][y] = '-'

            # 上下左右四个方向都遍历一遍
            dfs(x-1,y)
            dfs(x + 1,y)
            dfs(x ,y-1)
            dfs(x ,y+1)

        # 然后对边界上的O进行BFS
        for y in range(y_size):
            dfs(0,y)
            dfs(x_size-1,y)
        for x in range(1,x_size-1):
            dfs(x, 0)
            dfs(x, y_size-1)

        # 最后， -改为o ， o改为x
        for i in range(x_size):
            for j in range(y_size):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-':
                    board[i][j] = 'O'





s = Solution()
a = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(a)
print(a)