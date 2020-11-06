#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/3 11:35
# @Author : lantianyun l30001819
# @File : 226_invertTree.py

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
            return root
