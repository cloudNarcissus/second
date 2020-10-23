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
        # 题意是只有满足[low,high]的节点才保留下来，当某个节点的值小于low的时候，那么此节点以及此节点的左孩子就该剪掉；同理当某个节点的值大于high的时候，此节点的右孩子就该剪掉

        if not root:  # 同样，有这个的目的是避免root.left 和 root.right出错
            return None

        if root.val < low:
            # 剪掉左孩子，直接把自己的右孩子顶上去，也就是返回给上层,这里就跟上面的不剪枝有区别了，上面不剪枝的时候，无论如何都要返回root自己，而这次是返回自己的右孩子
            return self.trimBST( root.right, low, high) # 当然肯定不能直接返回自己的右孩子了，因为自己的右孩子能不能满足条件还得再过一遍函数
        if root.val > high:
            # 道理跟上面一样，这次是返回左孩子
            return self.trimBST(root.left, low, high)
        else:
            # 接下来就是本节点满足值域范围的情况，那就是直接把自己的左孩子设置成左树最终的根，也就是跟上面进行联动
            root.left = self.trimBST( root.left, low, high)
            # 右边一样
            root.right = self.trimBST(root.right, low, high)
            # 惯例返回自己
            return root


if __name__ == "__main__":
    bst = BST(nums=[1,2,3,4],root=None)
    print(bst.layerScan())

    s = Solution()
    root = s.trimBST(bst.root,0,0)

    bst2 = BST(nums=None, root=root)
    print(bst.layerScan())