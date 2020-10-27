#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/27 19:30
# @Author : lantianyun l30001819
# @File : 538_convertBST.py

# 所有节点的值变为右子树的累计值

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.num = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root:
            self.convertBST(root.right)
            root.val += self.num
            self.num = root.val
            self.convertBST(root.left)

        return root
