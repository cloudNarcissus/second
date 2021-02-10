#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/1/20 9:24
# @Author : lantianyun l30001819
# @File : minCostConnectPoints.py


from typing import List
from itertools import combinations
class Solution:
    def __init__(self):
        self.arr = []
        self.root = {}
        self.rootlen = {}
        self.edge = 0
        self.cost = 0

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 构建边

        for item in combinations([(i,j[0],j[1]) for i,j in enumerate(points)], 2):
            self.arr.append([item[0][0], item[1][0], abs(item[0][1] - item[1][1]) + abs(item[0][2] - item[1][2])]) # 前两位是点号，第三位是距离


        # 按照距离从小到大排序
        self.root = {i: i for (i, j) in enumerate(points)}
        self.rootlen = {i: 1 for (i, j) in enumerate(points)}
        self.arr.sort(key=lambda x:x[2])
        #print(self.arr)
        #print(self.root)

        # 查某个点的根节点
        def findroot(x):
            if self.root[x] != x:
                return findroot(self.root[x])
            return x

        def union(roota,rootb):
            if self.rootlen[roota] >= self.rootlen[rootb]:
                s_root, d_root = rootb ,roota
            else:
                s_root, d_root = roota, rootb

            for k,v in self.root.items():
                if s_root == v :
                    self.root[k] = d_root
                    self.rootlen[d_root] += 1
                    self.rootlen[s_root] -= 1
                    if self.rootlen[s_root] <= 0 :
                        break


        for pointa , pointb , d in self.arr:
            pointa_root , pointb_root = findroot(pointa),  findroot(pointb)
            if pointa_root != pointb_root:
                union(pointa_root , pointb_root)
                self.edge += 1
                self.cost += d
            else: # 否则说明已经在同一棵树中了
                pass

            # 直到边数达到n-1，则说明全连通了
            if self.edge == len(points) -1:
                break

        return self.cost





s = Solution()
print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))