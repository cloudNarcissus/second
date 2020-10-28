#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/28 17:23
# @Author : lantianyun l30001819
# @File : 124_maxPathSum.py
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None

        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root
    return level(0)


binary_tree = list_to_binarytree([-10,9,20,None,None,15,7])


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        if root.left:
            left_sum = self.maxPathSum(root.left)
        else:
            left_sum = -sys.maxsize - 1
        if root.right:
            right_sum = self.maxPathSum(root.right)
        else:
            right_sum = -sys.maxsize - 1

        return max(root.val, left_sum + root.val, right_sum + root.val, left_sum + right_sum + root.val)


s = Solution()
print(s.maxPathSum(binary_tree))