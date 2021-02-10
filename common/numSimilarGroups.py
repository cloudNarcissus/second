#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/18 16:58
# @Author : lantianyun l30001819
# @File : numSimilarGroups.py


from typing import List
from itertools import combinations
from collections import deque

strs = ["tars","rats","arts","star"]


class Solution:
    def __init__(self):
        self.cnt = 0

    def numSimilarGroups(self, strs: List[str]) -> int:
        self.strs = set(strs)
        self.len_ = len(strs[0])

        while self.strs:
            word = self.strs.pop()
            self.get_similar(word)
            self.cnt += 1

        return self.cnt


    def get_similar(self,word):
        queue = deque()
        queue.append(word)
        while queue and self.strs:
            word = queue.popleft()
            for  i in combinations([i for i in range(self.len_)],2):
                word_new = list(word[:])
                word_new[i[0]],word_new[i[1]] = word_new[i[1]],word_new[i[0]]
                word_new = ''.join(word_new)
                if word_new in self.strs:
                    self.strs.remove(word_new)
                    queue.append(word_new)


s = Solution()
print(s.numSimilarGroups(strs))




