#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/2 14:41
# @Author : lantianyun l30001819
# @File : 230_1202.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        pass

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k

        # 二叉搜索树，左<中<右, 采用中序遍历，直到k变为0为止
        def scan(root):
            if root:
                scan(root.left)
                self.k -= 1
                if self.k == 0:
                    self.res = root.val
                scan(root.right)

        scan(root)
        return self.res

