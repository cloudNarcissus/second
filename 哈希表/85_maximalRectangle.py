#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/28 13:13
# @Author : lantianyun l30001819
# @File : 85_maximalRectangle.py


class Solution:
    def __init__(self):
        self.s_max = 0  # 面积最大值

    def maximalRectangle(self, matrix) -> int:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    continue
                self.inner_matrix(i, j, matrix)

        return self.s_max

    def inner_matrix(self, i, j, matrix):
        row_min = None  # 每行最小值
        for x in range(i, len(matrix)):
            row = 0
            if matrix[x][j] == "0":  # 剪枝
                break
            for y in range(j, len(matrix[0])):
                if matrix[x][y] == "0":
                    break
                else:
                    row += 1
            row_min = self.get_rowmin(row_min, row)
            self.s_max = max(self.s_max, (x - i + 1) * row_min)

    def get_rowmin(self, row_min, row):
        return min(row_min, row) if row_min is not None else row


matrix = [["1", "0", "1", "1", "1"],
          ["0", "1", "0", "1", "0"],
          ["1", "1", "0", "1", "1"],
          ["1", "1", "0", "1", "1"],
          ["0", "1", "1", "1", "1"]]
s = Solution()
print(s.maximalRectangle(matrix))
