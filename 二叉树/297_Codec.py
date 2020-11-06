#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/3 16:02
# @Author : lantianyun l30001819
# @File : 297_Codec.py


# Definition for a binary tree node.

# 以下用BFS序列化二叉树和反序列化，主要用到双端队列

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            cur = q.popleft()
            if cur:
                res.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            else:
                res.append("None")

        return ",".join(map(str, res))

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

    @classmethod
    def deserialize2(self, data):
        """
        根据二叉树的性质，根节点的index的左孩子为index*2+1,右孩子为index*2+2 （这个方法只适用于满二叉树或者每个节点都加上了None）
        :param data:
        :return:
        """
        if data == "":  # 空串直接返回None
            return None
        nums = data.split(',')

        def create_root(index):
            if index >= len(nums) or nums[index] == "None":
                return None

            root = TreeNode(nums[index])
            root.left = create_root(index * 2 + 1)
            root.right = create_root(index * 2 + 2)
            return root

        return create_root(0)


root = Codec.deserialize2("1,2,3,None,None,4,5,None,None,None,None")
pass

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
