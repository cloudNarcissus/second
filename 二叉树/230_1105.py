#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/5 17:30
# @Author : lantianyun l30001819
# @File : 230_1105.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = None
        def mid_scan(root):
            nonlocal k,res
            if root and res is None:
                mid_scan(root.left)
                k -= 1
                if k <= 0:
                    res = root.val
                    return
                mid_scan(root.right)

        mid_scan(root)
        return res

class Solution2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        def scan(root):
            if root:
                yield scan(root.left)
                yield root.val
                yield scan(root.right)

        it = scan(root)
        for i in range(k):
            res = next(it)
        return res

