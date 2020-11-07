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

        x_size = len(board)
        if x_size <= 1:
            return board
        y_size = len(board[0])
        if x_size <= 1:
            return board

        def bfs(x, y):
            # 深度遍历的退出条件：超出矩阵边界或者值不为O
            if not 0 <= x < x_size or 0 <= y < y_size or board[x][y] != 'O':
                return

            # 遍历之后设置值为-，表示没有被包围，因为参与深度遍历的起始节点就是边界上的O
            board[x][y] = '-'

            # 上下左右四个方向都遍历一遍
            bfs[x-1][y]
            bfs[x + 1][y]
            bfs[x ][y-1]
            bfs[x ][y+1]

        # 然后对边界上的O进行BFS
        for y in range(y_size):
            bfs(0,y)
            bfs(x_size-1,y)
        for x in range(1,x_size-1):
            bfs(x, 0)
            bfs(x, y_size-1)

        # 最后， -改为o ， o改为x
        for i in range(x_size):
            for j in range(y_size):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-':
                    board[i][j] = 'O'






        for i in range(x_size):
            for j in




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