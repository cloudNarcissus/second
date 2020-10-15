#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/10/14 20:30
# @Author : lantianyun l30001819
# @File : 524_findLongestWord.py

# 给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。


from typing import List
import copy
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # 题目要求先按照长度排序，然后按照字典顺序排序，即多重排序
        # 多重排序，用sort先按优先级低的排，然后再按优先级高的排


        d.sort() # 先按低优先级的字典顺序从小到大排序
        d.sort(key=len,reverse=True) # 再按高优先级的字符长度从大到小排序
        sl = list(s) # 把源字符串散成字符列表

        for dest in d: # 遍历目标字符串列表
            dl = list(dest) # 把目标字符串散成字符列表
            i = 0 # 指向源字符串的指针
            j = 0 # 指向目标字符串的指针
            while j < len(dl) and i < len(sl): #任何一个字符串遍历完毕就退出循环
                if sl[i] == dl[j]: # 如果字符相等，则两个指针都前移
                    i = i+1
                    j = j+1
                else: # 否则目标指针不动，移动源指针
                    i = i + 1
            if j == len(dl):# 若上面的循环结束后，最终目标字符遍历完毕就说明源字符包含了目标串，满足条件
                return dest
        else:# 若目标字串都没有满足条件的，就返回空串
            return ""
