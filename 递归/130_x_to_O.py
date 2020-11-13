#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/6 19:37
# @Author : lantianyun l30001819
# @File : 130_x_to_O.py

from functools import lru_cache


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
y
        x_size = len(board)
        if x_size <= 1:
            return board
        y_size = len(board[0])
        if x_size <= 1:
            return board

        @lru_cache()
        def modify_to_x(x, y, depend_x, depend_y):  # (depend_x, depend_y) 是 (x, y) 依赖的节点
            nonlocal board
            # 如果是X则不替换
            if board[x][y] == 'X':
                return False
            # 如果O出现在边界，则不替换
            elif board[x][y] == 'O' and (x == 0 or y == 0 or x == x_size - 1 or y == y_size - 1):
                return False
            # 如果O的上下左右都是X，则替换
            elif board[x][y] == 'O' and board[x][y - 1] == 'X' and board[x][y + 1] == 'X' and board[x - 1][y] == 'X' and \
                    board[x + 1][y] == 'X':
                board[x][y] = 'X'
                return True
                # 否则
            else:
                if board[x][y - 1] == 'O' and ((x, y - 1) != (depend_x, depend_y)):
                    return False
                if board[x][y + 1] == 'O' and not modify_to_x(x, y + 1, x, y):
                    return False
                if board[x - 1][y] == 'O' and ((x - 1, y) != (depend_x, depend_y)):
                    return False
                if board[x + 1][y] == 'O' and not modify_to_x(x + 1, y, x, y):
                    return False
                board[x][y] = 'X'
                return True

        for i in range(x_size):
            for j in range(y_size):
                modify_to_x(i, j, 0, 0)


s = Solution()
a = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(a)
print(a)