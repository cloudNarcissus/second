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















# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
from itertools import combinations
def find_sum_n(k, n):
    return [list(i) for i in combinations([1,2,3,4,5,6,7,8,9], k) if sum(i)==n]


print(find_sum_n(3,9))







