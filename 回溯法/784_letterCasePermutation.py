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