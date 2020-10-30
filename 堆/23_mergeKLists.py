#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/30 16:22
# @Author : lantianyun l30001819
# @File : 23_mergeKLists.py


# 合并K个升序的链表

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        onelist = []
        for list in lists:
            point = list # 指针指向链表的head
            while point:
                onelist.append(point.val)
                point = point.next

        onelist.sort()

        head = None
        tail = head
        for item in onelist:
            if head:
                tail.next = ListNode(item)
                tail = tail.next
            else:
                head = ListNode(item)
                tail = head
        return head




