#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/26 16:11
# @Author : lantianyun l30001819
# @File : 230_kthSmallest.py


# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

# 该题就是中序遍历，只是增加了一个全局变量k

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def scan(root):
            nonlocal k
            if root.left:
                temp = scan(root.left)
                if temp is not None:
                    return temp
            if root:
                temp = root.val
                k -= 1
                if k == 0:
                    return temp
            if root.right:
                return scan(root.right)

        return scan(root)



class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def scan(root):
            if root is not None:
                yield from scan(root.left)
                yield root
                yield from scan(root.right)

        iterator = scan(root)
        for i in range(k):
            res = next(iterator).val
        return res



