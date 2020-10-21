#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/20 19:23
# @Author : lantianyun l30001819
# @File : list2link.py

# 两个函数，链表转list， list转链表

# 转了链表以后可以方便查找、排序等。（148.排序列表）

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None



def list_2_link(l):
    head = None
    if l:
        head = ListNode(l[0])
        cur = head
        for i in range(1,len(l)):
            cur.next = ListNode(l[i])
            cur = cur.next
    return head

def link_2_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        l = link_2_list(head)
        l.sort()
        return list_2_link(l)
