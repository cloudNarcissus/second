#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/28 19:22
# @Author : lantianyun l30001819
# @File : 94_inorderTraversal.py

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


binary_tree = list_to_binarytree([])


from typing import List

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        stack.append(root)
        while stack:
            cur = stack[-1]
            if not cur:
                return []
            if cur.left:
                stack.append(cur.left)
                cur.left = None

            else:
                cur=stack.pop()
                res.append(cur.val)
                if cur.right:
                    stack.append(cur.right)

        return res


s = Solution()
print(s.inorderTraversal(binary_tree))