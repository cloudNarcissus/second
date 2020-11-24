#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/21 16:24
# @Author : lantianyun l30001819
# @File : 22_generateParenthesis.py


class Solution:
    def generateParenthesis(self, n: int) :

        from itertools import permutations

        kuohao = '(' * n + ')' * n
        kuohao_set = set()
        res = []

        for i in permutations(kuohao, n * 2):
            kuohao_set.add(''.join(list(i)))

        return kuohao_set

        for one in kuohao_set:
            if self.isvalid(one):
                res.append(one)

        return res

    def isvalid(self, s):
        while s and '()' in s:
            s = s.replace('()', '')
        if s:
            return False
        else:
            return True



from itertools import product
for i in product('()', '()', '()', '()', '()', '()','()', '()', '()', '()', '()', '()'):
    print(i)
