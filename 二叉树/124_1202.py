#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/2 15:55
# @Author : lantianyun l30001819
# @File : 124_1202.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):

        from collections import deque
        q = deque()
        res = []

        def bfs(root):
            if root:
                q.append(root)
            while q:
                root = q.popleft()
                res.append(root.val if root else None)
                if root:
                    q.append(root.left)
                    q.append(root.right)

        return ",".join(["None" if i is None else str(i) for i in res])

    def deserialize(self, data):
        data_list = [None if i == "None" else i for i in data.split(',')]
        if data_list==['']:
            return None
        from collections import deque
        q = deque()
        i = 0
        q.append(self.init(data_list[i]))
        root = None
        while q:
            node = q.popleft()
            if root is None:
                root = node
            if node:
                i += 1
                left = self.init(data_list[i])
                node.left = left
                q.append(left)
                i += 1
                right = self.init(data_list[i])
                node.right = right
                q.append(right)
        return root


    def init(self,x):
        if x:
            return TreeNode(x)
        else:
            return None