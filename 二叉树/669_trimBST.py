#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/22 19:45
# @Author : lantianyun l30001819
# @File : 669_trimBST.py

# 遍历二叉树。

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self,nums:List=None,root=None):
        self.root = None
        if nums is not None:
            for num in nums:
                self.root=self.insert(self.root,num)
        elif root is not None:
            self.root = root


    def insert(self,root, val):
        """二叉搜索树的插入"""
        if not root:  # 一直到没有节点（即None）的时候，才生成新的节点
            root = TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)

        return root  # 最终返回的是根节点

    def insertList(self,nums:List):
        for num in nums:
            self.root=self.insert(self.root,num)
        return self.root


    def layerScan(self):
        """二叉搜索树的层序遍历"""
        """层序遍历的结果可以直接在力扣669中进行树结构可视化"""
        from collections import deque  # 引入双端队列，目的是层序遍历（又叫广度遍历BFS）
        res = []
        q = deque()
        if not self.root:
            return res
        q.append(self.root)

        while q:
            cur_node = q.popleft()
            res.append(cur_node.val)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)

        return res



# 接下来做669：bst剪枝

class Solution:
    def trimBST_not(self, root: TreeNode, low: int, high: int) -> TreeNode:

        # 如果不剪枝，怎样遍历这颗树呢？
        if not root:  # 有这个的目的是避免root.left 和 root.right出错
            return None
        # 接下来我们把二叉树就看成三个节点的一个小结构，即只有root， root.left , root.right
        # 下面三句话构成一个嵌套结构，即返回的root，就是左右子节点。
        # 写代码的时候，只要想着，我本次函数就返回一个root，这个方法将会应用在我的左右孩子节点上。
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right,low,high)
        return root

    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # 接下来我们看怎么剪枝。

if __name__ == "__main__":
    bst = BST(nums=[1,2,3,4],root=None)
    print(bst.layerScan())

    s = Solution()
    root = s.trimBST(bst.root,0,0)

    bst2 = BST(nums=None, root=root)
    print(bst.layerScan())