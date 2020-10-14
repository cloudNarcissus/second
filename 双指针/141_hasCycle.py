#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/14 19:45
# @Author : lantianyun l30001819
# @File : 141_hasCycle.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        i = head
        j = head  # i，j就像操场上跑圈的两个人，从起点出发
        while i and j and j.next and j.next.next:  #如果没有路了，就退出循环，说明没有环
            j= j.next.next # 否则j就跑两步
            i = i.next # i就跑一步
            if (i == j): # 如果操场是环状的，j肯定会超过i一整圈，从而两人再次相遇
                return True

        return False
