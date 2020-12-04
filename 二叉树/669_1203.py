#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/3 10:22
# @Author : lantianyun l30001819
# @File : 669_1203.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 裁剪搜索树，使其节点满足范围[low high]

class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if root:
            if root.val > high:  # 1. 仅左节点满足
                return self.trimBST(root.left, low, high)
            elif root.val <= high and root.val >= low:  # 2. 根节点满足
                root.left = self.trimBST(root.left, low, high)
                root.right = self.trimBST(root.right, low, high)
                return root
            elif root.val < low :  # 3. 仅右节点满足
                return self.trimBST(root.right, low, high)
        else:
            return None
