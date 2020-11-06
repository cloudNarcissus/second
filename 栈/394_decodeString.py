#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/6 10:26
# @Author : lantianyun l30001819
# @File : 394_decodeString.py

class Solution:
    def __init__(self):
        self.stack = []

    def decodeString(self, s: str) -> str:
        res = []
        for char in s:
            if char == "]":
                # 遇到右括号就出栈,然后把组好的字符串再入栈
                new_str = self.repeat()
                if new_str:
                    res.append(new_str)
            elif char.isdigit() or char == "[" or self.stack:
                # 数字、左括号以及栈不为空的时候的普通字符都入栈
                self.stack.append(char)
            else:
                # 如果栈为空，将普通字符放入结果
                res.append(char)
        # 最后把结果字串合起来
        return "".join(res)

    def repeat(self):
        temp_str = []
        temp_num = []
        char = self.stack.pop()
        while char != '[':
            temp_str.insert(0, char)
            char = self.stack.pop()
        char = self.stack[-1]
        while char and char.isdigit():
            temp_num.insert(0, self.stack.pop())
            if self.stack:
                char = self.stack[-1]
            else:
                char = None
        new_str = int("".join(temp_num)) * ("".join(temp_str))
        if self.stack:
            # 不为空则继续压入
            self.stack_append(new_str)
            return None
        else:
            # 栈为空则返回串，把这个返回串加入res
            return new_str

    def stack_append(self, new_str):
        self.stack.append(new_str)