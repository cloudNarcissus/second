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

    @classmethod
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        root = None
        if data == "":  # 空串直接返回None
            return root

        nums = data.split(',')
        num = nums.pop(0)  # 根节点特殊处理
        root = TreeNode(num)

        from collections import deque
        q = deque()

        q.append(root)  # 构造队列，然后根节点压入以便启动循环

        while q:
            p = q.popleft()  # 每弹出一个节点，就从原列表中取走前两个数字，分别是左和右的值
            left = nums.pop(0)
            right = nums.pop(0)
            left_node = TreeNode(left) if left != "None" else None  # 如果取出的是None，则说明没有左或右孩子，否则构造左右孩子节点
            right_node = TreeNode(right) if right != "None" else None
            if left_node:  # 如果有左孩子或者右孩子，需要把孩子压入队列
                q.append(left_node)
            if right_node:
                q.append(right_node)
            p.left = left_node
            p.right = right_node

        return root

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
root = Solution.deserialize("-10,9,20,None,None,15,7,None,None,None,None")
print(s.maxPathSum(binary_tree))