#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/20 19:44
# @Author : lantianyun l30001819
# @File : 784_letterCasePermutation.py

from typing import List

import itertools

class Solution:
    @classmethod
    def letterCasePermutation(self, S: str) -> List[str]:
        ss = []
        for s in S:
            if s.isdigit():
                ss.append(str(s))
            else:
                ss.append(s.upper()+s.lower())

        stuple = tuple(ss)

        res = []
        for i in itertools.product(*stuple):
            res.append(''.join(list(i)))

        return res

print(Solution.letterCasePermutation("a1b2"))


# 方法二，用dfs实现回溯

class Solution2:
    def letterCasePermutation(self, S: str) -> List[str]:

        len_ = len(S)
        res = []

        def dfs(start, onestr):  # start代表当前所在字符串的位置，onestr代表已经生成的子串
            if start >= len_ :  # 如果字符串遍历完毕，则退出递归，并把当前的子串放入结果中。
                res.append(onestr)
                return

            if S[start].isdigit(): # 遇到数字，只有一条路
                dfs(start + 1, onestr + S[start])

            else: # 遇到字母，有两条路，一条是大写路，一条是小写路
                dfs(start + 1, onestr + S[start].lower())
                dfs(start + 1, onestr + S[start].upper())

        dfs(0, "")

        return res





